from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import glob
from difflib import SequenceMatcher
import unicodedata
import re
import webbrowser
import threading
import uvicorn
import os
if os.name == 'nt':
    os.system('')  # Activa colores ANSI en cmd de Windows

app = FastAPI()

# Montar carpeta de templates y static
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# ╔═══════════════════════════════════════════╗
# ║              CONFIGURACIÓN                ║
# ╚═══════════════════════════════════════════╝

VERBOSE = True                     # ✅ Activa o desactiva logs de debug
UMBRAL_COINCIDENCIA = 0.65         # 🎯 Coincidencia mínima (70%)
EARLY_STOP_THRESHOLD = 94.0        # 🚀 Detener búsqueda si >= 94%
BLOQUE_TAMANO = 30                 # 📦 Tamaño de bloque para búsqueda intercalada

# 🎨 Colores ANSI para logs
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

#..............................................................................

def debug_log(msg, color=None):
    if VERBOSE:
        if color:
            print(f"{color}{msg}{RESET}")
        else:
            print(msg)

def cargar_langui():
    try:
        with open("LangUI.json", 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        debug_log("⚠️ LangUI.json no encontrado o inválido. Usando valores por defecto.", color=YELLOW)
        return {}

class ValidadorConsultas:
    def __init__(self):
        self.carpeta_consultas = os.path.join(os.getcwd(), "Consultas")
        self.archivos_json = self.encontrar_archivos_json()
        self.variaciones = self.cargar_variaciones_de_todos_archivos()
        self.umbral_coincidencia = UMBRAL_COINCIDENCIA
        self.exclusiones = self.cargar_exclusiones()
        debug_log(f"📂 {len(self.archivos_json)} archivos JSON cargados", color=CYAN)
        debug_log(f"📝 {len(self.variaciones)} frases cargadas", color=CYAN)
        debug_log(f"⚙️  Umbral de coincidencia base: {self.umbral_coincidencia * 100:.1f}%", color=CYAN)

    def cargar_exclusiones(self):
        try:
            with open("Exclusiones.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {
                    "inicio": [self.normalizar_texto(frase, False) for frase in data.get("inicio", [])],
                    "palabras": [self.normalizar_texto(palabra, False) for palabra in data.get("palabras", [])]
                }
        except (FileNotFoundError, json.JSONDecodeError):
            return {"inicio": [], "palabras": []}

    def encontrar_archivos_json(self):
        return glob.glob(os.path.join(self.carpeta_consultas, "*.json"))

    def cargar_variaciones_de_todos_archivos(self):
        todas_variaciones = []
        for archivo in self.archivos_json:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    todas_variaciones.extend(data.get("perfectas", []))
                    todas_variaciones.extend(data.get("con_errores", []))
            except json.JSONDecodeError:
                continue
        return todas_variaciones

    def normalizar_texto(self, texto, limpiar_exclusiones=True):
        texto = unicodedata.normalize('NFKD', texto.lower())
        texto = ''.join(c for c in texto if not unicodedata.combining(c))
        texto = texto.strip("¿¡?¡!.,").strip()
        if limpiar_exclusiones:
            palabras = texto.split()
            palabras = [p for p in palabras if p not in self.exclusiones["palabras"]]
            texto = " ".join(palabras)
        return texto

    def comparar_textos(self, texto1, texto2):
        clean1 = re.sub(r"[\s¿¡?.,!]", "", texto1)
        clean2 = re.sub(r"[\s¿¡?.,!]", "", texto2)
        ratio_chars = SequenceMatcher(None, clean1, clean2).ratio()
        set1 = set(texto1.split())
        set2 = set(texto2.split())
        interseccion = set1 & set2
        ratio_palabras = len(interseccion) / max(len(set2), 1)
        return max(ratio_chars, ratio_palabras)

    def ordenar_archivos_por_prioridad(self, consulta):
        consulta_norm = self.normalizar_texto(consulta)
        prioritarios = []
        no_prioritarios = []

        for archivo in self.archivos_json:
            archivo_nombre = os.path.basename(archivo)
            archivo_nombre_limpio = re.sub(r"\(Q\d+\),\s*", "", archivo_nombre).replace(".json", "")
            frases_clave = [
                self.normalizar_texto(p.strip(), limpiar_exclusiones=False)
                for p in archivo_nombre_limpio.split(",")
                if p.strip() and not p.startswith("(Q")
            ]
            if any(frase in consulta_norm for frase in frases_clave):
                prioritarios.append(archivo)
            else:
                no_prioritarios.append(archivo)

        debug_log(f"📦 Archivos prioritarios: {len(prioritarios)} / Total: {len(self.archivos_json)}", color=CYAN)
        if prioritarios:
            debug_log("📑 Lista de archivos prioritarios:", color=YELLOW)
            for p in prioritarios:
                debug_log(f"   - {os.path.basename(p)}", color=YELLOW)

        return prioritarios + no_prioritarios

    def buscar_coincidencia(self, consulta):
        coincidencias = []
        archivos_ordenados = self.ordenar_archivos_por_prioridad(consulta)
        debug_log(f"🔄 Procesando archivos en bloques de {BLOQUE_TAMANO}", color=CYAN)

        for i in range(0, len(archivos_ordenados), BLOQUE_TAMANO):
            bloque = archivos_ordenados[i:i+BLOQUE_TAMANO]
            for archivo in bloque:
                try:
                    with open(archivo, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        variantes = data.get("perfectas", []) + data.get("con_errores", [])
                        for variante in variantes:
                            contiene_exclusiones = any(
                                palabra in self.normalizar_texto(variante, limpiar_exclusiones=False).split()
                                for palabra in self.exclusiones["palabras"]
                            )
                            consulta_norm = self.normalizar_texto(consulta, limpiar_exclusiones=not contiene_exclusiones)
                            variante_norm = self.normalizar_texto(variante, limpiar_exclusiones=False)
                            similitud = self.comparar_textos(consulta_norm, variante_norm)

                            nombre_archivo = os.path.basename(archivo)
                            frases_clave = [
                                self.normalizar_texto(p.strip(), limpiar_exclusiones=False)
                                for p in nombre_archivo.split(",")
                                if p.strip() and not p.startswith("(Q")
                            ]
                            frases_encontradas = [f for f in frases_clave if f in consulta_norm]
                            bonus = len(frases_encontradas) * 0.2

                            if frases_encontradas:
                                debug_log(f"⭐ Frases clave coincidentes: {frases_encontradas} (+{bonus*100:.1f}%)", color=YELLOW)

                            indice_final = (similitud + bonus) * 100
                            color = GREEN if indice_final > 100 else YELLOW if indice_final >= 77 else RED
                            debug_log(
                                f"   → Comparando con: '{variante}' en {nombre_archivo}\n"
                                f"     Índice base: {similitud*100:.2f}% | Índice FINAL (con bonus): {indice_final:.2f}%",
                                color=color
                            )

                            coincidencias.append({
                                "variante": variante,
                                "archivo": archivo,
                                "puntaje": indice_final / 100
                            })

                            if indice_final >= EARLY_STOP_THRESHOLD:
                                debug_log(f"🚀 Early stop: coincidencia ≥{EARLY_STOP_THRESHOLD}% encontrada.", color=GREEN)
                                return {
                                    "variante": variante,
                                    "archivo": archivo,
                                    "puntaje": indice_final / 100
                                }
                except json.JSONDecodeError:
                    continue

        coincidencias.sort(key=lambda x: x["puntaje"], reverse=True)
        if coincidencias:
            mejor = coincidencias[0]
            color = GREEN if mejor['puntaje']*100 > 100 else YELLOW
            debug_log(f"✅ Mejor coincidencia: '{mejor['variante']}' ({mejor['puntaje']*100:.2f}%) en {os.path.basename(mejor['archivo'])}", color=color)
        else:
            debug_log("❌ No se encontraron coincidencias.", color=RED)

        return coincidencias[0] if coincidencias else None

    def obtener_respuesta(self, archivo):
        match = re.search(r"\((Q\d+)\)", archivo)
        if match:
            clave = match.group(1)
            try:
                with open("Respuestas.json", 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get("Respuestas", {}).get(clave)
            except (FileNotFoundError, json.JSONDecodeError):
                return None
        return None

    def validar_consulta(self, consulta):
        resultado = self.buscar_coincidencia(consulta)
        langui = cargar_langui()
        if resultado:
            indice_pct = resultado["puntaje"] * 100
            if indice_pct >= 100 or indice_pct >= self.umbral_coincidencia * 100:
                debug_log(f"🎯 Coincidencia aceptada: {indice_pct:.2f}%", color=GREEN if indice_pct >= 100 else YELLOW)
                respuesta = self.obtener_respuesta(resultado["archivo"])
                return respuesta or langui.get("NoSabe", "Lo siento. No dispongo de esa información.")
            else:
                debug_log(f"❌ Coincidencia insuficiente: {indice_pct:.2f}% < {self.umbral_coincidencia*100:.1f}%", color=RED)
        else:
            debug_log("❌ Ninguna coincidencia encontrada.", color=RED)
        return langui.get("NoSabe", "Lo siento. No dispongo de esa información.")

validador = ValidadorConsultas()

#..............................................................................

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    langui = cargar_langui()
    return templates.TemplateResponse("index.html", {"request": request, "langui": langui})

@app.post("/consulta")
async def consulta(data: dict):
    consulta_texto = data.get("consulta", "")
    respuesta = validador.validar_consulta(consulta_texto)
    return JSONResponse({"respuesta": respuesta})

@app.get("/admin", response_class=HTMLResponse)
async def admin(request: Request):
    langui = cargar_langui()
    try:
        with open("Respuestas.json", 'r', encoding='utf-8') as f:
            respuestas = json.load(f).get("Respuestas", {})
    except (FileNotFoundError, json.JSONDecodeError):
        respuestas = {}
    try:
        with open("Lang.json", 'r', encoding='utf-8') as f:
            lang = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        lang = {}
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "respuestas": respuestas,
        "lang": lang,
        "langui": langui
    })

@app.post("/guardar_respuestas")
async def guardar_respuestas(data: dict):
    nuevas_respuestas = data.get("respuestas", {})
    try:
        with open("Respuestas.json", 'w', encoding='utf-8') as f:
            json.dump({"Respuestas": nuevas_respuestas}, f, ensure_ascii=False, indent=2)
        return JSONResponse({"status": "success", "message": "Respuestas guardadas correctamente."})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

#..............................................................................

def abrir_navegador():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1.0, abrir_navegador).start()
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
