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
        """Extrae palabras clave de los nombres de archivo (separadas por comas)"""
        palabras_clave = {}
        for archivo in self.archivos_json:
            nombre = os.path.splitext(archivo)[0]
            palabras = [p.strip().lower() for p in nombre.split(',') if p.strip()]
            palabras_clave[archivo] = palabras
        return palabras_clave

    def encontrar_archivos_json(self):
        """Busca todos los archivos JSON en la carpeta actual"""
        archivos = glob.glob('*.json')
        if not archivos:
            raise FileNotFoundError("No se encontraron archivos JSON en la carpeta")
        print(f"📂 Archivos JSON encontrados: {', '.join(archivos)}")
        return archivos

    def cargar_variaciones_de_todos_archivos(self):
        """Carga variaciones de todos los archivos JSON encontrados"""
        todas_variaciones = []
        for archivo in self.archivos_json:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    todas_variaciones.extend(data.get("perfectas", []))
                    todas_variaciones.extend(data.get("con_errores", []))
                    print(f"📊 Cargadas {len(data.get('perfectas', [])) + len(data.get('con_errores', []))} variaciones de {archivo}")
            except json.JSONDecodeError as e:
                print(f"⚠️ Error al leer {archivo}: {str(e)}")
                continue
        return todas_variaciones

    def normalizar_texto(self, texto):
        """Normaliza el texto para comparación sin distinción de mayúsculas/acentos"""
        texto = unicodedata.normalize('NFKD', texto.lower())
        texto = ''.join(c for c in texto if not unicodedata.combining(c))
        return texto.strip("¿¡").strip("?¡!.,")

    def calcular_ajuste_archivo(self, consulta_norm, archivo):
        """Calcula el ajuste por palabras clave en el nombre del archivo"""
        ajuste = 0
        for palabra in self.palabras_clave_archivos.get(archivo, []):
            if palabra in consulta_norm:
                ajuste += 0.15  # 15% por cada palabra clave coincidente
        return min(ajuste, 0.3)  # Máximo 30% de ajuste

    def buscar_coincidencia(self, consulta):
        """Busca la mejor coincidencia usando comparación difusa con ajustes por archivo"""
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
                        
                        # Aplicar ajuste por palabras clave en el nombre del archivo
                        ajuste = self.calcular_ajuste_archivo(consulta_norm, archivo)
                        similitud_ajustada = min(similitud + ajuste, 1.0)  # No puede superar 100%

                        if similitud_ajustada > mejor_puntaje:
                            mejor_puntaje = similitud_ajustada
                            mejor_coincidencia = variante
                            mejor_archivo = archivo
                            if mejor_puntaje >= 1.0:  # Coincidencia exacta
                                break

            except json.JSONDecodeError:
                continue

        return mejor_coincidencia, mejor_puntaje, mejor_archivo

    def obtener_respuesta(self, archivo):
        """Obtiene la respuesta asociada a la clave QX del nombre de archivo"""
        clave = archivo.split(',')[0].strip("()")  # Extraer QX del nombre: "(Q1), algo.json" -> Q1
        try:
            with open("Respuestas.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                respuesta = data.get("Respuestas", {}).get(clave)
                if respuesta:
                    print(f"💬 Respuesta encontrada ({clave}): {respuesta}")
                else:
                    print(f"⚠️ No se encontró la clave '{clave}' en Respuestas.json")
        except FileNotFoundError:
            print("❌ No se encontró el archivo Respuestas.json")
        except json.JSONDecodeError:
            print("❌ Error al leer Respuestas.json")

    def validar_consulta(self, consulta):
        """Valida una consulta e imprime resultados detallados"""
        if not consulta.strip():
            print("⚠️ Por favor ingrese una consulta válida")
            return

        coincidencia, puntaje, archivo = self.buscar_coincidencia(consulta)

        if puntaje >= self.umbral_coincidencia:
            tipo = "PERFECTA" if puntaje >= 0.99 else "VÁLIDA"
            print(f"\n✅ {tipo} (Coincidencia: {puntaje*100:.1f}%)")
            print(f"   Consulta original: '{consulta}'")
            print(f"   Variante encontrada: '{coincidencia}'")
            print(f"   Archivo fuente: '{archivo}'")
            self.obtener_respuesta(archivo)
        else:
            print("\n❌ Consulta no reconocida")
            print(f"   Mejor coincidencia encontrada: {puntaje*100:.1f}%")
            if puntaje > 0.6:
                print(f"   ¿Quizás quisiste decir: '{coincidencia}'?")
            else:
                print("   Prueba con: '¿Hay habitaciones disponibles?' o similar")

def main():
    print("\n🔍 Validador Inteligente de Consultas (con vínculo a Respuestas.json)")
    print("---------------------------------------------------------------------")
    
    try:
        validador = ValidadorConsultas()
        print(f"\n🔄 Total de variaciones cargadas: {len(validador.variaciones)}")
    except Exception as e:
        print(f"\n❌ Error inicial: {str(e)}")
        print("Asegúrese de tener archivos JSON en la misma carpeta")
        return

    while True:
        try:
            consulta = input("\nIngrese su consulta (o 'salir' para terminar): ").strip()
            if consulta.lower() == 'salir':
                break
                
            validador.validar_consulta(consulta)
        except KeyboardInterrupt:
            print("\n\n🔚 Programa terminado por el usuario")
            break
        except Exception as e:
            print(f"\n⚠️ Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()
