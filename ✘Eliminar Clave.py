import os
import json
import glob

def pedir_qx():
    """Pide solo el número de QX y devuelve como (QX)"""
    while True:
        user_input = input("🔢 Introduce solo el número de QX a eliminar (ej. 102): ").strip()
        if user_input.isdigit():
            return f"(Q{int(user_input)})"  # Devuelve (Q102)
        print("❌ Entrada inválida. Solo números. Ejemplo válido: 102")

def eliminar_entrada_json(archivo, clave):
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ {archivo} está corrupto. No se puede procesar.")
                return
        # Eliminar en Respuestas o directamente según estructura
        if "Respuestas" in data and isinstance(data["Respuestas"], dict):
            if clave in data["Respuestas"]:
                del data["Respuestas"][clave]
                with open(archivo, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"🗑️ Eliminado {clave} de {archivo}")
            else:
                print(f"ℹ️ {clave} no encontrado en {archivo}")
        else:
            if clave in data:
                del data[clave]
                with open(archivo, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"🗑️ Eliminado {clave} de {archivo}")
            else:
                print(f"ℹ️ {clave} no encontrado en {archivo}")
    else:
        print(f"📄 {archivo} no existe.")

def eliminar_archivo_por_patron(carpeta, patron):
    archivos = glob.glob(os.path.join(carpeta, patron))
    if archivos:
        for archivo in archivos:
            os.remove(archivo)
            print(f"🗑️ Archivo eliminado: {archivo}")
    else:
        print(f"ℹ️ No se encontró ningún archivo en {carpeta} con patrón {patron}")

def main():
    qx = pedir_qx()

    eliminar_entrada_json("Respuestas.json", qx)
    eliminar_entrada_json("Lang.json", qx)

    eliminar_archivo_por_patron("Consultas", f"{qx},*.json")
    eliminar_archivo_por_patron("Training", f"{qx},*.py")

    print("\n✅ Proceso de eliminación finalizado.")

if __name__ == "__main__":
    main()
