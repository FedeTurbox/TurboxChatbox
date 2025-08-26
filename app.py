from fastapi import FastAPI, Request, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import glob
from difflib import SequenceMatcher
import unicodedata
import re
import os
import shutil # Importar la librería shutil

# --- Nuevas importaciones para la IA y scripts locales ---
from sentence_transformers import SentenceTransformer, util
import torch
from generador_lib import ejecutar_generacion
from Eliminar_Clave import ejecutar_eliminacion
import nltk # <--- AÑADIDO PARA LA DIVISIÓN INTELIGENTE

if os.name == 'nt':
    os.system('')

app = FastAPI()

templates = Jinja2Templates(directory="templates")
# Montamos el directorio 'static' completo
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- Funciones para manejar la configuración del tema ---
def get_instance_config(instance_id: int) -> dict:
    """Carga la configuración de una instancia, incluyendo el tema."""
    instance_path = os.path.join("Instancias", str(instance_id))
    config_path = os.path.join(instance_path, "config.json")
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    # Devuelve una configuración por defecto si no existe o hay error
    return {"theme": "Moderno"} # ACTUALIZADO: El valor por defecto ahora es "Moderno"

def save_instance_config(instance_id: int, config: dict):
    """Guarda la configuración de una instancia."""
    instance_path = os.path.join("Instancias", str(instance_id))
    os.makedirs(instance_path, exist_ok=True)
    config_path = os.path.join(instance_path, "config.json")
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

def get_available_themes() -> list:
    """Escanea el directorio de temas y devuelve una lista de los disponibles."""
    themes_dir = os.path.join("static", "Themes")
    if not os.path.isdir(themes_dir):
        return []
    return [d for d in os.listdir(themes_dir) if os.path.isdir(os.path.join(themes_dir, d))]

# --- Lógica de la IA y el Validador ---

class AIResponder:
    """
    Gestiona la carga del modelo de IA y la búsqueda de respuestas semánticas
    en un documento de texto.
    """
    def __init__(self, instance_path):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"🤖 AIResponder: Usando dispositivo '{self.device}'.")
        model_name = 'paraphrase-multilingual-MiniLM-L12-v2'
        try:
            self.model = SentenceTransformer(model_name, device=self.device)
            print(f"✅ Modelo de IA '{model_name}' cargado correctamente.")
        except Exception as e:
            self.model = None
            print(f"❌ ERROR al cargar el modelo de IA: {e}")
            return
        self.document_path = os.path.join(instance_path, 'informacion_adicional.txt')
        self.corpus_chunks = []
        self.corpus_embeddings = None
        self._load_and_process_document()

    def _split_into_chunks(self, text: str, max_chunk_length: int = 600) -> list[str]:
        """
        Divide el texto en fragmentos (chunks) de manera más inteligente.
        Primero divide por párrafos. Si un párrafo es demasiado largo,
        lo subdivide en grupos de oraciones.
        """
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            print("📥 Descargando tokenizador de oraciones de NLTK ('punkt')...")
            nltk.download('punkt', quiet=True)

        text = text.replace('\r\n', '\n')
        initial_chunks = re.split(r'\n{2,}', text)
        
        final_chunks = []
        for chunk in initial_chunks:
            chunk = chunk.strip()
            if len(chunk) == 0:
                continue
            
            if len(chunk) > max_chunk_length:
                print(f"쪼개기 Chunk demasiado largo ({len(chunk)} chars). Dividiendo en oraciones...")
                sentences = nltk.sent_tokenize(chunk, language='spanish')
                current_sub_chunk = ""
                for sentence in sentences:
                    if len(current_sub_chunk) + len(sentence) + 1 < max_chunk_length:
                        current_sub_chunk += sentence + " "
                    else:
                        if current_sub_chunk:
                            final_chunks.append(current_sub_chunk.strip())
                        current_sub_chunk = sentence + " "
                if current_sub_chunk:
                    final_chunks.append(current_sub_chunk.strip())
            else:
                final_chunks.append(chunk)

        meaningful_chunks = [c for c in final_chunks if len(c) > 20]
        print(f"📝 Texto dividido en {len(meaningful_chunks)} fragmentos finales.")
        return meaningful_chunks

    def _load_and_process_document(self):
        if not self.model or not os.path.exists(self.document_path): return
        try:
            with open(self.document_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.corpus_chunks = self._split_into_chunks(content)
            
            if not self.corpus_chunks: 
                print("⚠️ No se encontraron fragmentos de texto significativos en el documento.")
                return

            print(f"📚 Procesando {len(self.corpus_chunks)} fragmentos del documento de conocimiento...")
            self.corpus_embeddings = self.model.encode(self.corpus_chunks, convert_to_tensor=True, device=self.device)
            print("👍 Documento de conocimiento procesado y listo para consultas.")
        except Exception as e:
            print(f"❌ ERROR procesando el documento de IA: {e}")

    def _normalize_for_boost(self, text: str) -> str:
        """
        Normalización simplificada para la comparación de títulos.
        Convierte a minúsculas, elimina acentos y puntuación.
        """
        text_norm = unicodedata.normalize('NFKD', text.lower()).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        text_norm = re.sub(r'[^\w\s]', '', text_norm)
        return text_norm

    def answer_question(self, question, top_k=5, score_threshold=0.30, title_boost=0.25):
        """
        Busca una respuesta combinando búsqueda semántica con un impulso de puntuación
        para las coincidencias de título, solucionando el sesgo hacia fragmentos más largos.
        """
        if self.corpus_embeddings is None or not self.corpus_chunks: return None

        question_embedding = self.model.encode(question, convert_to_tensor=True, device=self.device)
        
        hits = util.semantic_search(question_embedding, self.corpus_embeddings, top_k=top_k)[0]
        
        if not hits:
            return None

        # --- Lógica de Re-ranking con Impulso de Título ---
        boosted_hits = []
        normalized_question_words = set(self._normalize_for_boost(question).split())

        for hit in hits:
            chunk_text = self.corpus_chunks[hit['corpus_id']]
            # Considera las primeras 7 palabras como el "título" del fragmento
            chunk_title_words = set(self._normalize_for_boost(chunk_text).split()[:7])
            
            # Si TODAS las palabras de la consulta están en el título del fragmento, aplica un impulso fuerte
            if normalized_question_words.issubset(chunk_title_words):
                boosted_score = hit['score'] + title_boost
                print(f"🚀 Impulso FUERTE aplicado a '{chunk_text[:30]}...' de {hit['score']:.2f} a {boosted_score:.2f}")
                hit['score'] = boosted_score
            
            boosted_hits.append(hit)

        # Vuelve a ordenar los resultados con las puntuaciones actualizadas
        sorted_hits = sorted(boosted_hits, key=lambda x: x['score'], reverse=True)

        print(f"🔍 Resultados Re-clasificados: {[ (h['score'], self.corpus_chunks[h['corpus_id']][:40] + '...') for h in sorted_hits]}")

        # Devuelve el mejor resultado si supera el umbral de confianza
        best_hit = sorted_hits[0]
        if best_hit['score'] > score_threshold:
            print(f"✅ Coincidencia final encontrada con puntaje {best_hit['score']:.2f}")
            return self.corpus_chunks[best_hit['corpus_id']]
        
        print(f"❌ Ninguna coincidencia superó el umbral de {score_threshold}. La mejor fue de {best_hit['score']:.2f}")
        return None

class ValidadorConsultas:
    """
    Gestiona la lógica de validación de consultas basada en reglas (archivos JSON).
    Ahora recibe una instancia de AIResponder en lugar de crearla.
    """
    def __init__(self, instance_id: int, ai_responder: AIResponder):
        self.instance_id = instance_id
        self.instance_path = os.path.join(os.getcwd(), "Instancias", str(instance_id))
        self.exclusiones = self._load_json_global("Exclusiones.json")
        self.respuestas = self._load_json_instancia("Respuestas.json").get("Respuestas", {})
        self.ai_responder = ai_responder

    def _load_json_global(self, filename):
        path = os.path.join(os.getcwd(), filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _load_json_instancia(self, filename):
        path = os.path.join(self.instance_path, filename)
        if not os.path.exists(path): return {}
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def normalizar_texto(self, texto, limpiar_exclusiones=True):
        texto_norm = unicodedata.normalize('NFKD', texto.lower()).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        texto_norm = texto_norm.strip("¿¡?¡!.,").strip()
        if limpiar_exclusiones:
            palabras = texto_norm.split()
            palabras_excluir = self.exclusiones.get("palabras", [])
            palabras = [p for p in palabras if p not in palabras_excluir]
            texto_norm = " ".join(palabras)
        return texto_norm

    def comparar_textos(self, texto1, texto2):
        return SequenceMatcher(None, texto1, texto2).ratio()

    def buscar_coincidencia_reglas(self, consulta):
        consulta_norm = self.normalizar_texto(consulta)
        mejor_coincidencia = {"puntaje": 0}
        
        carpeta_consultas = os.path.join(self.instance_path, "Consultas")
        if not os.path.isdir(carpeta_consultas): return None

        for archivo_path in glob.glob(os.path.join(carpeta_consultas, "*.json")):
            try:
                with open(archivo_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                variantes = data.get("perfectas", []) + data.get("con_errores", [])
                for variante in variantes:
                    variante_norm = self.normalizar_texto(variante, False)
                    similitud = self.comparar_textos(consulta_norm, variante_norm)
                    if similitud > mejor_coincidencia["puntaje"]:
                        mejor_coincidencia = {"variante": variante, "archivo": archivo_path, "puntaje": similitud}
            except (json.JSONDecodeError, FileNotFoundError):
                continue
        
        return mejor_coincidencia if mejor_coincidencia["puntaje"] > 0.65 else None

    def obtener_respuesta_reglas(self, archivo):
        match = re.search(r"\((Q\d+)\)", archivo)
        if match:
            clave_q = match.group(1)
            return self.respuestas.get(clave_q)
        return None

    def procesar_consulta(self, consulta):
        if not os.path.isdir(self.instance_path):
            langui = self._load_json_global("LangUI.json")
            return langui.get("NoSabe", "No he podido encontrar una respuesta.")

        resultado_reglas = self.buscar_coincidencia_reglas(consulta)
        langui = self._load_json_global("LangUI.json")
        
        if resultado_reglas:
            respuesta = self.obtener_respuesta_reglas(resultado_reglas["archivo"])
            return respuesta or langui.get("NoSabe", "Respuesta para la regla no encontrada.")
        
        respuesta_ia = self.ai_responder.answer_question(consulta)
        if respuesta_ia:
            return respuesta_ia
        
        return langui.get("NoSabe", "No he podido encontrar una respuesta.")

# --- Dos cachés separadas para la IA y las reglas ---
ai_responders_cache = {}
validadores_cache = {}

def get_ai_responder(instance_id: int) -> AIResponder:
    """Crea o recupera un AIResponder de la caché."""
    if instance_id not in ai_responders_cache:
        print(f"🧠 Creando y cacheando AIResponder para la instancia {instance_id}...")
        instance_path = os.path.join(os.getcwd(), "Instancias", str(instance_id))
        ai_responders_cache[instance_id] = AIResponder(instance_path)
    return ai_responders_cache[instance_id]

def get_validador(instance_id: int) -> ValidadorConsultas:
    """Crea o recupera un ValidadorConsultas de la caché, inyectando el AIResponder cacheado."""
    if instance_id not in validadores_cache:
        print(f"룰 Creando y cacheando ValidadorConsultas para la instancia {instance_id}...")
        ai_responder = get_ai_responder(instance_id)
        validadores_cache[instance_id] = ValidadorConsultas(instance_id, ai_responder)
    return validadores_cache[instance_id]

# --- ENDPOINTS ---

@app.get("/{instance_id}", response_class=HTMLResponse)
async def read_root(request: Request, instance_id: int):
    validador = get_validador(instance_id)
    langui = validador._load_json_global("LangUI.json")
    config = get_instance_config(instance_id)
    selected_theme = config.get("theme", "Moderno") # ACTUALIZADO
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "langui": langui, 
        "instance_id": instance_id,
        "selected_theme": selected_theme
    })

@app.post("/{instance_id}/consulta")
async def consulta(instance_id: int, data: dict):
    validador = get_validador(instance_id)
    consulta_texto = data.get("consulta", "")
    respuesta = validador.procesar_consulta(consulta_texto)
    return JSONResponse({"respuesta": respuesta})

@app.get("/{instance_id}/admin", response_class=HTMLResponse)
async def admin(request: Request, instance_id: int):
    validador = get_validador(instance_id)
    respuestas = validador.respuestas
    lang = validador._load_json_instancia("Lang.json")
    langui = validador._load_json_global("LangUI.json")
    
    claves_ordenadas = sorted(respuestas.keys(), key=lambda q: int(re.sub(r'\D', '', q)))
    respuestas_ordenadas = {k: respuestas[k] for k in claves_ordenadas}
    
    config = get_instance_config(instance_id)
    selected_theme = config.get("theme", "Moderno") # ACTUALIZADO
    available_themes = get_available_themes()
    
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "respuestas": respuestas_ordenadas,
        "lang": lang,
        "langui": langui,
        "instance_id": instance_id,
        "selected_theme": selected_theme,
        "available_themes": available_themes
    })

@app.post("/{instance_id}/admin/guardar")
async def guardar_configuracion(instance_id: int, data: dict):
    instance_path = os.path.join("Instancias", str(instance_id))
    if not os.path.isdir(instance_path):
        raise HTTPException(status_code=404, detail=f"La instancia {instance_id} no existe.")

    try:
        if "respuestas" in data:
            nuevas_respuestas = data.get("respuestas", {})
            respuestas_path = os.path.join(instance_path, "Respuestas.json")
            respuestas_data = {"Respuestas": {}}
            if os.path.exists(respuestas_path):
                with open(respuestas_path, 'r', encoding='utf-8') as f:
                    try:
                        respuestas_data = json.load(f)
                    except json.JSONDecodeError:
                        pass
            
            if "Respuestas" not in respuestas_data or not isinstance(respuestas_data["Respuestas"], dict):
                respuestas_data["Respuestas"] = {}
            respuestas_data["Respuestas"].update(nuevas_respuestas)
            with open(respuestas_path, 'w', encoding='utf-8') as f:
                json.dump(respuestas_data, f, ensure_ascii=False, indent=2)

        if "theme" in data:
            nuevo_tema = data.get("theme")
            if nuevo_tema and nuevo_tema in get_available_themes():
                config = get_instance_config(instance_id)
                config["theme"] = nuevo_tema
                save_instance_config(instance_id, config)
        
        if instance_id in validadores_cache:
            print(f"♻️  Limpiando caché de Validador (instancia {instance_id}) por guardado de configuración.")
            del validadores_cache[instance_id]
            
        return JSONResponse({"status": "success", "message": "Configuración guardada correctamente."})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

@app.post("/{instance_id}/admin/upload_info")
async def upload_info(instance_id: int, file: UploadFile = File(...)):
    instance_path = os.path.join("Instancias", str(instance_id))
    os.makedirs(instance_path, exist_ok=True)

    if file.content_type != 'text/plain':
        raise HTTPException(status_code=400, detail="El archivo debe ser de tipo .txt")

    file_path = os.path.join(instance_path, "informacion_adicional.txt")
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        if instance_id in validadores_cache:
            print(f"♻️  Limpiando caché de Validador (instancia {instance_id}) por subida de archivo de conocimiento.")
            del validadores_cache[instance_id]
        if instance_id in ai_responders_cache:
            print(f"♻️  Limpiando caché de AIResponder (instancia {instance_id}) por subida de archivo de conocimiento.")
            del ai_responders_cache[instance_id]
            
        return JSONResponse({
            "status": "success",
            "message": "Archivo de conocimiento actualizado correctamente"
        })
    except Exception as e:
        return JSONResponse({
            "status": "error",
            "message": f"No se pudo guardar el archivo: {e}"
        }, status_code=500)

@app.post("/{instance_id}/admin/generar")
async def generar_nueva_consulta(instance_id: int, data: dict):
    frase_base = data.get("frase_base")
    respuesta_base = data.get("respuesta_base")

    if not frase_base or not respuesta_base:
        raise HTTPException(status_code=400, detail="La frase base y la respuesta no pueden estar vacías.")

    descripcion_usuario = frase_base
    respuesta_inicial = respuesta_base
    
    resultado = ejecutar_generacion(
        instance_id=instance_id,
        frase_base=frase_base,
        respuesta_usuario=respuesta_inicial,
        descripcion_usuario=descripcion_usuario
    )
    
    if resultado.get("status") == "success":
        if instance_id in validadores_cache:
            print(f"♻️  Limpiando caché de Validador (instancia {instance_id}) por generación de nueva consulta.")
            del validadores_cache[instance_id]
        return JSONResponse(resultado)
    else:
        raise HTTPException(status_code=500, detail=resultado.get("message", "Error desconocido durante la generación."))

@app.delete("/{instance_id}/admin/eliminar/{clave_q}")
async def eliminar_consulta(instance_id: int, clave_q: str):
    resultado = ejecutar_eliminacion(instance_id, clave_q)
    
    if resultado.get("status") == "success":
        if instance_id in validadores_cache:
            print(f"♻️  Limpiando caché de Validador (instancia {instance_id}) por eliminación de consulta.")
            del validadores_cache[instance_id]
        return JSONResponse(resultado)
    else:
        raise HTTPException(status_code=500, detail=resultado.get("message", "Error durante la eliminación."))
