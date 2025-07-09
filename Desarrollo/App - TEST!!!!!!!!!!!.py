import json
import os
import glob
from difflib import SequenceMatcher
import unicodedata

class ValidadorConsultas:
    def __init__(self):
        self.archivos_json = self.encontrar_archivos_json()
        self.variaciones = self.cargar_variaciones_de_todos_archivos()
        self.umbral_coincidencia = 0.9  # 90% de similitud
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
        if not archivos:
            raise FileNotFoundError("No se encontraron archivos JSON en la carpeta")
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
        return texto.strip("¿¡").strip("?¡!.,").strip()

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
        mejor_coincidencia = None
        mejor_puntaje = 0
        mejor_archivo = ""

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
                            if mejor_puntaje >= 1.0:
                                break
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
        if not consulta.strip():
            print("Por favor ingrese una consulta válida.")
            return

        coincidencia, puntaje, archivo = self.buscar_coincidencia(consulta)

        if puntaje >= self.umbral_coincidencia:
            respuesta = self.obtener_respuesta(archivo)
            if respuesta:
                print(respuesta)
            else:
                print("No se encontró respuesta asociada.")
        else:
            print("Lo siento. No dispongo de esa información. ¿Desea hablar con administración?")

def main():
    try:
        validador = ValidadorConsultas()
    except Exception as e:
        print(str(e))
        return

    # 🔥 Saludo inicial
    print("Bienvenido al servicio de respuesta automatizada del Hotel 5 Libertadores de América.")
    print("Escriba su consulta (o escriba 'salir' para finalizar):")

    while True:
        try:
            consulta = input("> ").strip()
            if consulta.lower() == 'salir':
                print("Gracias por usar el servicio. ¡Hasta pronto!")
                break
            validador.validar_consulta(consulta)
        except KeyboardInterrupt:
            print("\nGracias por usar el servicio. ¡Hasta pronto!")
            break
        except Exception:
            print("Ha ocurrido un error inesperado.")

if __name__ == "__main__":
    main()
