import os
import json
import glob
import shutil

def pedir_id_instancia():
    """Pide al usuario el ID de la instancia y valida que exista."""
    while True:
        instance_id = input("🆔 Introduce el ID de la instancia que quieres eliminar (ej. 1): ").strip()
        if instance_id.isdigit():
            instance_path = os.path.join(os.getcwd(), "Instancias", instance_id)
            if os.path.isdir(instance_path):
                return instance_id, instance_path
            else:
                print(f"❌ La carpeta para la instancia '{instance_id}' no existe en 'Instancias/'.")
        else:
            print("❌ Por favor, introduce un número válido.")

def confirmar(instance_id):
    """Pide confirmación al usuario de forma clara para una instancia específica."""
    print(f"\n⚠️  ADVERTENCIA: Esta acción es irreversible y eliminará los siguientes datos DE LA INSTANCIA '{instance_id}':")
    print("    - Todos los archivos en la carpeta 'Consultas'")
    print("    - Todos los archivos en la carpeta 'Training'")
    print("    - El archivo 'Respuestas.json'")
    print("    - El archivo 'Lang.json'")
    
    respuesta = input("\n    ¿Estás completamente seguro de que quieres continuar? (s/n): ").strip().lower()
    return respuesta == "s"

def limpiar_carpeta(ruta_carpeta):
    """Borra de forma segura todos los archivos y subcarpetas de una carpeta."""
    nombre_carpeta = os.path.basename(ruta_carpeta)
    print(f"\n--- Limpiando carpeta: '{nombre_carpeta}' ---")
    if not os.path.isdir(ruta_carpeta):
        print(f"📂 Información: La carpeta no existe. No hay nada que limpiar.")
        return

    elementos = glob.glob(os.path.join(ruta_carpeta, "*"))
    if not elementos:
        print("✅ La carpeta ya está vacía.")
        return

    for ruta_elemento in elementos:
        try:
            if os.path.isfile(ruta_elemento) or os.path.islink(ruta_elemento):
                os.remove(ruta_elemento)
                print(f"🗑️ Archivo eliminado: {os.path.relpath(ruta_elemento)}")
            elif os.path.isdir(ruta_elemento):
                shutil.rmtree(ruta_elemento)
                print(f"🗑️ Carpeta eliminada: {os.path.relpath(ruta_elemento)}")
        except Exception as e:
            print(f"❌ ERROR al eliminar '{ruta_elemento}': {e}")

def eliminar_archivo(ruta_archivo):
    """Elimina un archivo de forma segura."""
    nombre_archivo = os.path.basename(ruta_archivo)
    print(f"\n--- Intentando eliminar archivo: '{nombre_archivo}' ---")
    if not os.path.isfile(ruta_archivo):
        print(f"📄 Información: El archivo no existe. No hay nada que eliminar.")
        return
    
    try:
        os.remove(ruta_archivo)
        print(f"🗑️ Archivo eliminado: {nombre_archivo}")
    except Exception as e:
        print(f"❌ ERROR al eliminar '{nombre_archivo}': {e}")

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"📍 Ejecutando en el directorio: {os.getcwd()}\n")

    instance_id, instance_path = pedir_id_instancia()

    if confirmar(instance_id):
        print(f"\n🚨 Iniciando proceso de eliminación total para la instancia '{instance_id}'...\n")
        
        # Rutas específicas de la instancia
        ruta_consultas = os.path.join(instance_path, "Consultas")
        ruta_training = os.path.join(instance_path, "Training")
        ruta_respuestas = os.path.join(instance_path, "Respuestas.json")
        ruta_lang = os.path.join(instance_path, "Lang.json")
        
        limpiar_carpeta(ruta_consultas)
        limpiar_carpeta(ruta_training)
        eliminar_archivo(ruta_respuestas)
        eliminar_archivo(ruta_lang)
        
        print("\n✅ Proceso de eliminación finalizado.")
    else:
        print("\n❌ Operación cancelada por el usuario.")
    
    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    main()
