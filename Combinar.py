import os

def crear_copia_archivos_optimizada():
    """
    Crea un archivo de texto con un resumen estructurado para una IA,
    incluyendo contexto del proyecto y el contenido de archivos específicos
    (.py, .bat, .js, .jsx, .html, .css, .json)
    en el directorio actual y sus subcarpetas, excluyendo __pycache__ y venv.
    """

    # --- Configuración del script ---
    # Directorio raíz donde se ejecuta el script
    directorio_raiz = os.getcwd()

    # Tipos de archivo a incluir
    extensiones_incluidas = [".py", ".bat", ".js", ".jsx", ".html", ".css", ".json"]

    # Carpetas a excluir
    carpetas_excluidas = ["__pycache__", "venv", "Consultas", "Training"]

    # Nombre del archivo de salida
    nombre_archivo_salida = "Chatbot.txt"
    ruta_archivo_salida = os.path.join(directorio_raiz, nombre_archivo_salida)

    print("🚀 Iniciando la creación del archivo de contexto para IA.")
    print("---")
    
    # Marcador de posición para la descripción del proyecto.
    # El usuario debe editar manualmente el archivo de salida para agregar la descripción.
    descripcion_proyecto = "[AÑADIR AQUÍ: Una descripción general del proyecto. Explica su propósito, funcionalidades clave, y cualquier dependencia importante.]"

    print("\n---")
    print(f"🔍 Buscando extensiones: {', '.join(extensiones_incluidas)}")
    print(f"🚫 Excluyendo carpetas: {', '.join(carpetas_excluidas)}")
    print(f"💾 El contenido estructurado se guardará en: {ruta_archivo_salida}\n")

    archivos_procesados = []

    # --- Búsqueda y recopilación de archivos ---
    for carpeta_actual, subdirectorios, archivos in os.walk(directorio_raiz):
        subdirectorios[:] = [d for d in subdirectorios if d not in carpetas_excluidas]

        for archivo in archivos:
            _, extension = os.path.splitext(archivo)
            if extension.lower() in extensiones_incluidas:
                ruta_relativa = os.path.relpath(os.path.join(carpeta_actual, archivo), directorio_raiz)
                archivos_procesados.append(ruta_relativa)
                print("Encontrado: {ruta_relativa}")

    # --- Escritura del archivo de salida ---
    try:
        with open(ruta_archivo_salida, "w", encoding="utf-8") as archivo_salida:
            # 1. Título y Resumen del Proyecto
            archivo_salida.write("## Contexto del Proyecto\n")
            archivo_salida.write("### Descripción General\n")
            archivo_salida.write(descripcion_proyecto)
            archivo_salida.write("\n\n" + "=" * 80 + "\n")

            # 2. Índice o Listado de Archivos
            archivo_salida.write("## Estructura de Archivos\n")
            archivo_salida.write("A continuación, se listan todos los archivos incluidos en este documento:\n")
            for f in sorted(archivos_procesados):
                archivo_salida.write(f"- {f}\n")
            archivo_salida.write("\n" + "=" * 80 + "\n")

            # 3. Contenido de cada archivo
            archivo_salida.write("## Código Fuente Detallado\n")
            if not archivos_procesados:
                 archivo_salida.write("No se encontraron archivos para procesar.")

            for ruta_relativa in sorted(archivos_procesados):
                ruta_completa_archivo = os.path.join(directorio_raiz, ruta_relativa)
                try:
                    with open(ruta_completa_archivo, "r", encoding="utf-8") as f:
                        contenido = f.read()

                        # Sección para un comentario manual
                        archivo_salida.write(f"\n\n--- Archivo: {ruta_relativa} ---\n")
                        archivo_salida.write("\n### Rol del archivo: [AÑADIR AQUÍ UNA BREVE DESCRIPCIÓN MANUAL DEL ARCHIVO]\n\n")
                        archivo_salida.write(f"```\n{contenido}\n```\n")
                        archivo_salida.write("\n" + "-" * 80 + "\n") # Separador visual

                except Exception as e:
                    print(f"Error al leer '{ruta_relativa}': {e}")
            
        print(f"\n🎉 ¡Éxito! Se generó el archivo '{nombre_archivo_salida}' con una estructura optimizada para IA.")

    except Exception as e:
        print(f"\n🚨 ¡ERROR FATAL! No se pudo crear o escribir en '{nombre_archivo_salida}': {e}")
        print("Por favor, verifica los permisos de escritura en el directorio o si el archivo ya está abierto.")
    
    # Pausa para que el usuario pueda leer los mensajes
    input("\nPresiona Enter para cerrar la ventana...")

if __name__ == "__main__":
    crear_copia_archivos_optimizada()
