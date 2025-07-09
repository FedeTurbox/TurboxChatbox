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
        self.umbral_coincidencia = 0.9
        self.palabras_clave_archivos = self.extraer_palabras_clave()

    def extraer_palabras_clave(self):
        palabras_clave = {}
        for archivo in self.archivos_json:
            nombre = os.path.splitext(archivo)[0]
            palabras = [p.strip().lower() for p in nombre.split(',') if p.strip()]
            palabras_clave[archivo] = palabras
        return palabras_clave

    def encontrar_archivos_json(self):
        archivos = glob.glob('*.json')
        return archivos

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

    def normalizar_texto(self, texto):
        texto = unicodedata.normalize('NFKD', texto.lower())
        texto = ''.join(c for c in texto if not unicodedata.combining(c))
        texto = texto.strip("¿¡").strip("?¡!.,").strip()

        # Si la consulta tiene más de 15 caracteres, eliminar "gracias" y "por favor" con variantes
        if len(texto) > 15:
            # Expresiones regulares para detectar variantes de "gracias" y "por favor"
            patrones = [
                r"\bgr(a|á|à|ä|â)s?i(a|á|à|ä|â)?s\b",         # gracias, grasias, grásias, etc.
                r"\bpor\s*f(a|á|à|ä|â)v(a|á|à|ä|â)?(o|u)r\b", # por favor, porfabor, porfvor, etc.
                r"\bporfavor\b"                              # porfavor pegado
            ]
            for patron in patrones:
                texto = re.sub(patron, "", texto, flags=re.IGNORECASE)

            texto = " ".join(texto.split())  # Quitar espacios duplicados

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
