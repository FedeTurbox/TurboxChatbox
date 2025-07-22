import os
import json
import glob
import shutil

def confirmar():
    """Pide confirmación al usuario"""
    respuesta = input("⚠️ Esto eliminará TODOS los datos (Consultas, Training, Respuestas.json, Lang.json). ¿Estás seguro? (S/N): ").strip().lower()
    return respuesta == "s"

def limpiar_carpeta(carpeta):
    """Borra todos los archivos de la carpeta"""
    if os.path.exists(carpeta):
        archivos = glob.glob(os.path.join(carpeta, "*"))
        for archivo in archivos:
            if os.path.isfile(archivo):
                os.remove(archivo)
                print(f"🗑️ Archivo eliminado: {archivo}")
            elif os.path.isdir(archivo):
                shutil.rmtree(archivo)
                print(f"🗑️ Carpeta eliminada: {archivo}")
        print(f"✅ Todos los archivos eliminados en {carpeta}")
    else:
        print(f"📂 Carpeta {carpeta} no existe.")

def eliminar_json(archivo):
    """Elimina físicamente el archivo JSON"""
    if os.path.exists(archivo):
        os.remove(archivo)
        print(f"🗑️ Archivo eliminado: {archivo}")
    else:
        print(f"📄 Archivo {archivo} no existe.")

def main():
    if confirmar():
        print("\n🚨 Eliminando todos los datos...\n")
        limpiar_carpeta("Consultas")
        limpiar_carpeta("Training")
        eliminar_json("Respuestas.json")
        eliminar_json("Lang.json")
        print("\n✅ Eliminación completa.")
    else:
        print("\n❌ Operación cancelada por el usuario.")

if __name__ == "__main__":
    main()
