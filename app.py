from flask import Flask, request, jsonify, render_template
import json
import os
import glob
from difflib import SequenceMatcher
import unicodedata
import re

app = Flask(__name__)

class ValidadorConsultas:
    def __init__(self):
        self.archivos_json = self.encontrar_archivos_json()
        self.variaciones = self.cargar_variaciones_de_todos_archivos()
        self.umbral_coincidencia = 0.9  # UMBRAL DE SENSIBILIDAD
        self.palabras_clave_archivos = self.extraer_palabras_clave()
        self.exclusiones = self.cargar_exclusiones()

    def cargar_exclusiones(self):
        try:
            with open("Exclusiones.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {
                    "inicio": [self.normalizar_texto(frase, limpiar_exclusiones=False) for frase in data.get("inicio", [])],
                    "palabras": [self.normalizar_texto(palabra, limpiar_exclusiones=False) for palabra in data.get("palabras", [])]
                }
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ Exclusiones.json no encontrado o con errores. Continuando sin exclusiones.")
            return {"inicio": [], "palabras": []}

    def extraer_palabras_clave(self):
        palabras_clave = {}
        for archivo in self.archivos_json:
            nombre = os.path.splitext(archivo)[0]
            palabras = [p.strip().lower() for p in nombre.split(',') if p.strip()]
            palabras_clave[archivo] = palabras
        return palabras_clave

    def encontrar_archivos_json(self):
        return glob.glob('*.json')

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
        texto = texto.strip("¿¡").strip("?¡!.,").strip()

        if limpiar_exclusiones and hasattr(self, "exclusiones"):
            # Limpiar frases de inicio si la consulta es larga
            if len(texto) > 15:
                for frase in self.exclusiones["inicio"]:
                    if texto.startswith(frase):
                        texto = texto[len(frase):].strip()

            # Limpiar palabras sueltas en cualquier parte
            for palabra in self.exclusiones["palabras"]:
                patron = r"\b{}\b".format(re.escape(palabra))
                texto = re.sub(patron, "", texto, flags=re.IGNORECASE)

        texto = " ".join(texto.split())  # Quitar espacios extra
        return texto

    def calcular_ajuste_archivo(self, consulta_norm, archivo):
        ajuste = 0
        for palabra in self.palabras_clave_archivos.get(archivo, []):
            if palabra in consulta_norm:
                ajuste += 0.15
        return min(ajuste, 0.3)

    def buscar_coincidencia(self, consulta):
        if not self.variaciones:
            return None, 0, ""

        consulta_norm = self.normalizar_texto(consulta)
        mejor_coincidencia, mejor_puntaje, mejor_archivo = None, 0, ""

        for archivo in self.archivos_json:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    variantes = data.get("perfectas", []) + data.get("con_errores", [])

                    for variante in variantes:
                        variante_norm = self.normalizar_texto(variante)
                        similitud = SequenceMatcher(None, consulta_norm, variante_norm).ratio()

                        ajuste = self.calcular_ajuste_archivo(consulta_norm, archivo)
                        similitud_ajustada = min(similitud + ajuste, 1.0)

                        if similitud_ajustada > mejor_puntaje:
                            mejor_puntaje = similitud_ajustada
                            mejor_coincidencia = variante
                            mejor_archivo = archivo
            except json.JSONDecodeError:
                continue

        return mejor_coincidencia, mejor_puntaje, mejor_archivo

    def obtener_respuesta(self, archivo):
        clave = archivo.split(',')[0].strip("()")
        try:
            with open("Respuestas.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("Respuestas", {}).get(clave)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def validar_consulta(self, consulta):
        coincidencia, puntaje, archivo = self.buscar_coincidencia(consulta)
        if puntaje >= self.umbral_coincidencia:
            respuesta = self.obtener_respuesta(archivo)
            if respuesta:
                return respuesta
            else:
                return "No se encontró respuesta asociada."
        else:
            return "Lo siento. No dispongo de esa información. ¿Desea hablar con administración?"

validador = ValidadorConsultas()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/consulta", methods=["POST"])
def consulta():
    data = request.json
    consulta = data.get("consulta", "")
    respuesta = validador.validar_consulta(consulta)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
