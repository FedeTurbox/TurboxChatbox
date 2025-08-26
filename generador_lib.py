import json
import os
import shutil
from collections import OrderedDict
import random
import glob
import re
from itertools import product
import sys
import pickle

# Importaciones de NLTK
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import cess_esp as cess
from nltk.tag import UnigramTagger

# --- Global Dictionaries ---
CURATED_SYNONYMS = {}
QUESTION_TEMPLATES = {}
SPANISH_TAGGER = None
TAGGER_FILE = "spanish_tagger.pkl"

def cargar_diccionarios_globales():
    """Carga los diccionarios globales desde Diccionario.json."""
    global CURATED_SYNONYMS, QUESTION_TEMPLATES
    dict_path = os.path.join(os.getcwd(), "Diccionario.json")
    try:
        with open(dict_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            CURATED_SYNONYMS = data.get("curated_synonyms", {})
            QUESTION_TEMPLATES = data.get("question_templates", {})
            print(f"✅ Diccionarios globales cargados desde '{dict_path}'.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"🚨 ERROR al cargar Diccionario.json: {e}")
        CURATED_SYNONYMS = {}
        QUESTION_TEMPLATES = {}

def preparar_tagger_espanol():
    """Carga o entrena el tagger de español."""
    global SPANISH_TAGGER
    if SPANISH_TAGGER is not None:
        return
    if os.path.exists(TAGGER_FILE):
        with open(TAGGER_FILE, 'rb') as f:
            SPANISH_TAGGER = pickle.load(f)
    else:
        print("🔧 Creando y entrenando el analizador de español (esto solo pasará una vez)...")
        train_sents = cess.tagged_sents()
        tagger = UnigramTagger(train_sents)
        SPANISH_TAGGER = tagger
        with open(TAGGER_FILE, 'wb') as f:
            pickle.dump(tagger, f)
        print("✅ Analizador de español listo y guardado.")

def descargar_nltk_data():
    """Verifica y descarga los recursos de NLTK necesarios."""
    recursos = ['wordnet', 'omw-1.4', 'punkt', 'cess_esp']
    print("Verificando recursos de NLTK...")
    for recurso in recursos:
        try:
            if recurso == 'omw-1.4':
                 nltk.data.find(f'corpora/{recurso}.zip')
            elif recurso == 'punkt':
                 nltk.data.find(f'tokenizers/{recurso}.zip')
            else:
                 nltk.data.find(f'corpora/{recurso}.zip')
            print(f"  - '{recurso}' ya está disponible.")
        except LookupError:
            print(f"  - Descargando '{recurso}'...")
            nltk.download(recurso, quiet=False)
            print(f"  - '{recurso}' descargado.")

def obtener_sinonimos_wordnet(palabra):
    """Obtiene sinónimos de WordNet para una palabra en español."""
    sinonimos = set()
    for syn in wn.synsets(palabra, lang='spa'):
        for lemma in syn.lemmas(lang='spa'):
            sinonimo = lemma.name().replace('_', ' ')
            if sinonimo.lower() != palabra.lower():
                sinonimos.add(sinonimo)
    return list(sinonimos)

def crear_instancia_si_no_existe(instance_path, instance_id):
    """Crea la estructura de carpetas para una nueva instancia si no existe."""
    if not os.path.isdir(instance_path):
        print(f"📂 La instancia '{instance_id}' no existe. Creándola...")
        try:
            os.makedirs(os.path.join(instance_path, "Consultas"))
            os.makedirs(os.path.join(instance_path, "Training"))
            print(f"✅ Instancia '{instance_id}' creada.")
            return True
        except Exception as e:
            print(f"❌ ERROR al crear la instancia: {e}")
            return False
    return True

def normalizar_y_formatear_frase(frase, frase_original_base):
    frase = frase.strip().replace('?', '').replace('¿', '')
    if not frase: return ""
    palabras = frase.split(' ')
    primera_palabra_lower = palabras[0].lower()
    accent_map = {'cual': 'cuál', 'cuanto': 'cuánto', 'donde': 'dónde', 'que': 'qué', 'quien': 'quién'}
    palabras[0] = accent_map.get(primera_palabra_lower, primera_palabra_lower).capitalize()
    frase = " ".join(palabras)
    if primera_palabra_lower in QUESTION_TEMPLATES or frase_original_base.endswith('?'):
        frase = '¿' + frase + '?'
    return frase

def generar_variaciones_desde_frase_manual(frase_base):
    palabras_originales = nltk.word_tokenize(frase_base.lower().replace('?', ''), language='spanish')
    if not palabras_originales: return []
    frases_generadas = {normalizar_y_formatear_frase(frase_base, frase_base)}
    
    # --- LÓGICA DE SINÓNIMOS CORREGIDA ---
    componentes_combinados = {}
    # Lista de palabras comunes a ignorar durante la búsqueda de sinónimos
    stop_words_espanol = ['un', 'una', 'el', 'la', 'de', 'en', 'y', 'o', 'es', 'son', 'cuál', 'qué', 'me', 'del', 'al']

    for i, p in enumerate(palabras_originales):
        # --- CORRECCIÓN APLICADA AQUÍ ---
        # Si la palabra es una "stop word", se salta a la siguiente.
        if p in stop_words_espanol:
            continue

        sinonimos_curados = []
        # 1. Buscar en el diccionario manual
        for categoria, sinonimos_cat in CURATED_SYNONYMS.items():
            if p in sinonimos_cat:
                sinonimos_curados.extend(sinonimos_cat[p])
                break
        
        # 2. Buscar en WordNet
        sinonimos_wn = obtener_sinonimos_wordnet(p)
        
        # 3. Combinar y eliminar duplicados
        sinonimos_totales = list(set(sinonimos_curados + sinonimos_wn + [p]))
        
        if len(sinonimos_totales) > 1:
            componentes_combinados[i] = sinonimos_totales

    # Generar frases a partir de los componentes combinados
    if componentes_combinados:
        for combo in product(*[componentes_combinados[i] for i in componentes_combinados.keys()]):
            nueva_frase_lista = list(palabras_originales)
            for i_comp, reemplazo in enumerate(combo):
                nueva_frase_lista[list(componentes_combinados.keys())[i_comp]] = reemplazo
            frase_nueva = " ".join(nueva_frase_lista)
            frases_generadas.add(normalizar_y_formatear_frase(frase_nueva, frase_base))

    # Generar variaciones con plantillas de preguntas
    primera_palabra = palabras_originales[0]
    if primera_palabra in QUESTION_TEMPLATES:
        sujeto_frase = " ".join(palabras_originales[1:])
        for plantilla in QUESTION_TEMPLATES[primera_palabra]:
            frases_generadas.add(normalizar_y_formatear_frase(plantilla.format(sujeto=sujeto_frase), frase_base))

    return list(frases_generadas)


def siguiente_qx(instance_path):
    carpeta_consultas = os.path.join(instance_path, "Consultas")
    os.makedirs(carpeta_consultas, exist_ok=True)
    archivos = glob.glob(os.path.join(carpeta_consultas, "*.json"))
    numeros = [int(m.group(1)) for a in archivos if (m := re.search(r"\(Q(\d+)\)", a))]
    return f"(Q{max(numeros) + 1})" if numeros else "(Q1)"

def leer_json_seguro(ruta, clave_principal=None):
    if os.path.exists(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ {os.path.basename(ruta)} corrupto. Creando nuevo.")
    return {clave_principal: {}} if clave_principal else {}

def ordenar_por_q(diccionario):
    return OrderedDict(sorted(diccionario.items(), key=lambda item: int(re.sub(r"\D", "", item[0]))))

def guardar_respuesta_y_descripcion(instance_path, qx, respuesta_usuario, descripcion_usuario):
    q_num = qx.strip("()")
    
    archivo_respuestas = os.path.join(instance_path, "Respuestas.json")
    data = leer_json_seguro(archivo_respuestas, "Respuestas")
    if "Respuestas" not in data: data["Respuestas"] = {}
    data["Respuestas"][q_num] = respuesta_usuario
    data["Respuestas"] = ordenar_por_q(data["Respuestas"])
    with open(archivo_respuestas, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"📌 Respuesta guardada en {archivo_respuestas}")

    archivo_lang_instancia = os.path.join(instance_path, "Lang.json")
    lang_data = leer_json_seguro(archivo_lang_instancia)
    lang_data[q_num] = descripcion_usuario
    lang_data = ordenar_por_q(lang_data)
    with open(archivo_lang_instancia, 'w', encoding='utf-8') as f:
        json.dump(lang_data, f, ensure_ascii=False, indent=2)
    print(f"📌 Descripción guardada en {archivo_lang_instancia}")

def guardar_consultas_generadas(instance_path, frases_perfectas_base, nombre_base, n_a_seleccionar, qx):
    carpeta_consultas = os.path.join(instance_path, "Consultas")
    os.makedirs(carpeta_consultas, exist_ok=True)
    archivo_salida_json = os.path.join(carpeta_consultas, f"{qx}, {nombre_base}.json")
    perfectas = random.sample(frases_perfectas_base, min(len(frases_perfectas_base), n_a_seleccionar))
    with open(archivo_salida_json, 'w', encoding='utf-8') as f:
        json.dump({"perfectas": perfectas, "total": len(perfectas)}, f, ensure_ascii=False, indent=2)
    print(f"✅ Archivo JSON creado en: {archivo_salida_json}")

def obtener_palabras_clave(palabras):
    if not SPANISH_TAGGER: return []
    stop_words_espanol = ['un', 'una', 'el', 'la', 'de', 'en', 'y', 'o', 'es', 'son', 'cual', 'qué', 'me']
    functional_verbs = ['quiero', 'quisiera', 'deseo', 'necesito', 'tienen', 'tiene']
    etiquetas = SPANISH_TAGGER.tag(palabras)
    claves = [p for p, et in etiquetas if p.isalpha() and p not in stop_words_espanol and p not in functional_verbs]
    return list(OrderedDict.fromkeys(claves))

def ejecutar_generacion(instance_id, frase_base, respuesta_usuario, descripcion_usuario):
    """
    Función principal que encapsula todo el proceso de generación.
    Puede ser llamada desde el servidor web o desde la línea de comandos.
    """
    instance_path = os.path.join(os.getcwd(), "Instancias", str(instance_id))
    if not crear_instancia_si_no_existe(instance_path, instance_id):
        return {"status": "error", "message": f"No se pudo crear la instancia {instance_id}"}

    print(f"\n--- Iniciando generación para la instancia: {instance_id} ---")

    # Cargar recursos necesarios
    cargar_diccionarios_globales()
    descargar_nltk_data()
    preparar_tagger_espanol()
    
    palabras_tokenizadas = nltk.word_tokenize(frase_base.lower(), language='spanish')
    palabras_clave = obtener_palabras_clave(palabras_tokenizadas)
    nombre_base = ",".join(palabras_clave) if palabras_clave else frase_base.replace(" ", "_")[:20]
    
    qx = siguiente_qx(instance_path)
    
    frases_generadas = generar_variaciones_desde_frase_manual(frase_base)

    guardar_consultas_generadas(
        instance_path=instance_path,
        frases_perfectas_base=frases_generadas,
        nombre_base=nombre_base,
        n_a_seleccionar=len(frases_generadas),
        qx=qx
    )
    
    carpeta_training = os.path.join(instance_path, "Training")
    os.makedirs(carpeta_training, exist_ok=True)
    archivo_salida_py = os.path.join(carpeta_training, f"{qx}, {nombre_base}.py")
    script_original = os.path.abspath("NUEVA_FRSE.py")
    if os.path.exists(script_original):
        shutil.copy(script_original, archivo_salida_py)
        print(f"📝 Copia de NUEVA_FRASE.py guardada en: {archivo_salida_py}")

    guardar_respuesta_y_descripcion(instance_path, qx, respuesta_usuario, descripcion_usuario)

    print("\n🚀 Generación completada.")
    return {"status": "success", "message": f"Consulta {qx} generada con éxito.", "qx": qx}
