import os
import json
import glob
import shutil
import re

def eliminar_entrada_json(archivo, clave_q):
    """Elimina de forma segura una entrada de un archivo JSON."""
    if not os.path.isfile(archivo):
        print(f"📄 Información: El archivo '{os.path.basename(archivo)}' no existe.")
        return False
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print(f"⚠️  ERROR: El archivo '{os.path.basename(archivo)}' está corrupto.")
        return False

    clave_encontrada = False
    if "Respuestas" in data and isinstance(data.get("Respuestas"), dict) and clave_q in data["Respuestas"]:
        del data["Respuestas"][clave_q]
        clave_encontrada = True
    elif clave_q in data:
        del data[clave_q]
        clave_encontrada = True

    if not clave_encontrada:
        print(f"ℹ️  Información: La clave '{clave_q}' no se encontró en '{os.path.basename(archivo)}'.")
        return True # No es un error si la clave ya no está

    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"🗑️  Clave '{clave_q}' eliminada de '{os.path.basename(archivo)}'.")
    return True

def eliminar_archivos_por_patron(carpeta, patron):
    """Elimina archivos que coincidan con un patrón."""
    if not os.path.isdir(carpeta):
        return
    for archivo in glob.glob(os.path.join(carpeta, patron)):
        try:
            os.remove(archivo)
            print(f"🗑️  Archivo eliminado: {os.path.relpath(archivo)}")
        except Exception as e:
            print(f"❌ ERROR al eliminar '{archivo}': {e}")

def ejecutar_eliminacion(instance_id, clave_q):
    """
    Función principal que elimina todos los artefactos de una consulta (QX).
    Puede ser llamada desde otros scripts.
    """
    instance_path = os.path.join(os.getcwd(), "Instancias", str(instance_id))
    if not os.path.isdir(instance_path):
        return {"status": "error", "message": f"Instancia {instance_id} no encontrada."}

    print(f"\n🚨 Iniciando eliminación para '{clave_q}' en la instancia '{instance_id}'...")

    patron_q_json = f"({clave_q})*.json"
    patron_q_py = f"({clave_q})*.py"

    # Rutas específicas de la instancia
    ruta_respuestas = os.path.join(instance_path, "Respuestas.json")
    ruta_lang = os.path.join(instance_path, "Lang.json")
    ruta_consultas = os.path.join(instance_path, "Consultas")
    ruta_training = os.path.join(instance_path, "Training")

    # Ejecutar eliminaciones
    eliminar_entrada_json(ruta_respuestas, clave_q)
    eliminar_entrada_json(ruta_lang, clave_q)
    eliminar_archivos_por_patron(ruta_consultas, patron_q_json)
    eliminar_archivos_por_patron(ruta_training, patron_q_py)

    print(f"✅ Proceso de eliminación para '{clave_q}' finalizado.")
    return {"status": "success", "message": f"Consulta {clave_q} eliminada correctamente."}

if __name__ == "__main__":
    # --- MODO INTERACTIVO (para ejecutar el script directamente) ---
    def pedir_id_instancia():
        while True:
            instance_id = input("🆔 Introduce el ID de la instancia (ej. 1): ").strip()
            if instance_id.isdigit(): return instance_id
            print("❌ Por favor, introduce un número válido.")

    def pedir_qx():
        while True:
            user_input = input("🔢 Introduce solo el número de QX a eliminar (ej. 102): ").strip()
            if user_input.isdigit(): return f"Q{int(user_input)}"
            print("❌ Entrada inválida. Solo números.")

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"📍 Ejecutando en el directorio: {os.getcwd()}\n")

    id_instancia = pedir_id_instancia()
    clave_a_eliminar = pedir_qx()

    respuesta = input(f"\n    ¿Seguro que quieres eliminar '{clave_a_eliminar}' de la instancia '{id_instancia}'? (s/n): ").strip().lower()
    if respuesta == 's':
        ejecutar_eliminacion(id_instancia, clave_a_eliminar)
    else:
        print("\n❌ Operación cancelada.")

    input("\nPresiona Enter para salir...")
