import json
import os
import shutil
from collections import OrderedDict
import random
import glob
import re
from itertools import product

def siguiente_qx():
    carpeta_consultas = os.path.join(os.getcwd(), "Consultas")
    os.makedirs(carpeta_consultas, exist_ok=True)
    archivos = glob.glob(os.path.join(carpeta_consultas, "*.json"))
    numeros = [int(m.group(1)) for a in archivos if (m := re.search(r"\(Q(\d+)\)", a))]
    return f"(Q{max(numeros)+1})" if numeros else "(Q1)"

def pedir_qx():
    """Pide el número de QX o asigna automático."""
    while True:
        user_input = input("🔢 Introduce solo el número de QX (ej. 5) o deja vacío para asignar automáticamente: ").strip()
        if user_input == "":
            qx = siguiente_qx()
            print(f"✅ QX asignado automáticamente: {qx}")
            return qx
        if user_input.isdigit():
            qx = f"(Q{int(user_input)})"
            print(f"✅ QX definido: {qx}")
            return qx
        print("❌ Solo números. Ejemplo válido: 5")

def normalizar(texto):
    return texto.lower().strip()

def leer_json_seguro(ruta, clave_principal=None):
    """Lee un JSON y devuelve su contenido. Si no existe o está vacío, crea uno."""
    if os.path.exists(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
        except json.JSONDecodeError:
            print(f"⚠️ {os.path.basename(ruta)} corrupto o vacío. Creando nuevo.")
    return {clave_principal: {}} if clave_principal else {}

def ordenar_por_q(diccionario):
    """Ordena las claves Q por número ascendente"""
    return OrderedDict(sorted(
        diccionario.items(),
        key=lambda item: int(re.sub(r"\D", "", item[0]))
    ))

def expandir_frases_base(frases_base, max_frases=500):
    """Genera frases únicas solo a partir de frases base (sin extras)"""
    resultado = [fb.capitalize() for fb in frases_base]
    random.shuffle(resultado)
    if len(resultado) > max_frases:
        print(f"⚠️ Aviso: Total de frases ({len(resultado)}) excede max_frases ({max_frases}), recortando.")
        return resultado[:max_frases]
    return resultado

def generar_frases_dinamicas(verbos, adverbios, acciones, objetos, max_frases=500):
    """Genera frases combinando componentes lingüísticos"""
    combinaciones = set()
    for verbo, adverbio, accion, objeto in product(verbos, adverbios, acciones, objetos):
        frase = f"{verbo} {accion} {objeto}".strip()
        if adverbio:
            frase += f" {adverbio}"
        combinaciones.add(frase.capitalize())
    combinaciones = list(combinaciones)
    random.shuffle(combinaciones)
    return combinaciones[:max_frases]

def introducir_errores(frase, errores_comunes):
    """Introduce errores en cualquier coincidencia parcial"""
    nueva_frase = frase
    for palabra, variantes in errores_comunes.items():
        pattern = re.compile(re.escape(palabra), re.IGNORECASE)
        if pattern.search(nueva_frase) and random.random() < 0.6:
            nueva_frase = pattern.sub(random.choice(variantes), nueva_frase)
    if random.random() < 0.15:
        nueva_frase = nueva_frase.upper()
    elif random.random() < 0.15:
        nueva_frase = nueva_frase.capitalize()
    return nueva_frase

def guardar_respuesta_y_descripcion(qx, respuesta_usuario, descripcion_usuario):
    """Guarda respuesta y descripción en archivos JSON"""
    q_num = qx.strip("()")

    # 📌 Respuesta
    archivo_respuestas = os.path.abspath("Respuestas.json")
    data = leer_json_seguro(archivo_respuestas, "Respuestas")
    if q_num not in data["Respuestas"]:
        data["Respuestas"][q_num] = respuesta_usuario
        data["Respuestas"] = ordenar_por_q(data["Respuestas"])
        with open(archivo_respuestas, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"📌 Respuesta guardada en {archivo_respuestas}")
    else:
        print(f"🔹 Respuesta ya existe para {qx}")

    # 📌 Descripción
    archivo_lang = os.path.abspath("Lang.json")
    lang_data = leer_json_seguro(archivo_lang)
    if q_num not in lang_data:
        lang_data[q_num] = descripcion_usuario
        lang_data = ordenar_por_q(lang_data)
        with open(archivo_lang, 'w', encoding='utf-8') as f:
            json.dump(lang_data, f, ensure_ascii=False, indent=2)
        print(f"📌 Descripción guardada en {archivo_lang}")
    else:
        print(f"🔹 Descripción ya existe para {qx}")

def generar_con_errores(frases_base=None, errores_comunes=None, nombre_base="output",
                        frases_minimas=None, n_perfectas=150,
                        verbos=None, adverbios=None, acciones=None, objetos=None,
                        respuesta_usuario=None, descripcion_usuario=None, qx=None):
    """Genera frases perfectas y con errores"""
    carpeta_consultas = os.path.join(os.getcwd(), "Consultas")
    carpeta_training = os.path.join(os.getcwd(), "Training")
    os.makedirs(carpeta_consultas, exist_ok=True)
    os.makedirs(carpeta_training, exist_ok=True)

    # 🔥 Pedir QX si no se pasó
    if qx is None:
        qx = pedir_qx()
    else:
        print(f"✅ Usando QX recibido: {qx}")

    archivo_salida_json = os.path.join(carpeta_consultas, f"{qx}, {nombre_base}.json")
    archivo_salida_py = os.path.join(carpeta_training, f"{qx}, {nombre_base}.py")

    # ✅ Generar frases perfectas
    if frases_base:
        print("✅ Generando frases desde frases_base...")
        perfectas = expandir_frases_base(frases_base, max_frases=n_perfectas*2)
    elif all([verbos, adverbios, acciones, objetos]):
        print("✅ Generando frases desde componentes lingüísticos...")
        perfectas = generar_frases_dinamicas(verbos, adverbios, acciones, objetos, max_frases=n_perfectas*2)
    else:
        raise ValueError("Debe proporcionar frases_base o componentes lingüísticos (verbos, adverbios, acciones, objetos)")

    perfectas_set = set(normalizar(f) for f in perfectas[:n_perfectas])
    perfectas = perfectas[:n_perfectas]
    print(f"✅ Generadas {len(perfectas)} frases perfectas.")

    # ✅ Generar variantes con errores
    con_errores_set = set()
    con_errores = []
    intentos = 0
    while len(con_errores) < n_perfectas and intentos < n_perfectas * 5:
        intentos += 1
        frase = random.choice(perfectas)
        frase_err = introducir_errores(frase, errores_comunes or {})
        norm_frase = normalizar(frase_err)
        if norm_frase not in perfectas_set and norm_frase not in con_errores_set:
            con_errores.append(frase_err)
            con_errores_set.add(norm_frase)
    print(f"✅ Generadas {len(con_errores)} frases con errores.")

    # 💾 Guardar JSON
    with open(archivo_salida_json, 'w', encoding='utf-8') as f:
        json.dump({
            "perfectas": perfectas,
            "con_errores": con_errores,
            "total": len(perfectas) + len(con_errores)
        }, f, ensure_ascii=False, indent=2)
    print(f"✅ Archivo JSON creado en: {archivo_salida_json}")

    # 📋 Copiar NUEVA FRASE.py
    script_original = os.path.abspath("NUEVA_FRASE.py")
    if os.path.exists(script_original):
        shutil.copy(script_original, archivo_salida_py)
        print(f"📝 Copia de NUEVA FRASE.py guardada en: {archivo_salida_py}")
    else:
        print("⚠️ No se encontró NUEVA FRASE.py para copiar.")

    # ✍️ Pedir respuesta y descripción si no se pasaron
    if respuesta_usuario is None:
        respuesta_usuario = input(f"\n💬 Introduce la respuesta para {qx}: ").strip() or "Respuesta faltante"
    if descripcion_usuario is None:
        descripcion_usuario = input(f"\n📝 Introduce la descripción para {qx}: ").strip() or "String faltante"

    guardar_respuesta_y_descripcion(qx, respuesta_usuario, descripcion_usuario)

    print("\n🚀 Generación completada.")

if __name__ == "__main__":
    print("⚠️ Este módulo es una biblioteca. Úsalo importándolo desde otro script.")
    input("\n🔚 Presiona ENTER para salir...")
