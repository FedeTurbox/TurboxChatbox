import sys
from generador_lib import ejecutar_generacion

if __name__ == "__main__":
    # --- Manejo de Argumentos de Línea de Comandos ---
    if len(sys.argv) > 2:
        instance_id_arg = sys.argv[1]
        frase_base_arg = sys.argv[2]
        respuesta_usuario_arg = input(f"\n💬 Introduce la respuesta: ").strip() or "Respuesta faltante"
        # Usar la frase base como descripción por defecto si no se provee una
        descripcion_usuario_arg = input(f"\n📝 Introduce la descripción (dejar en blanco usa la frase base): ").strip() or frase_base_arg
        ejecutar_generacion(instance_id_arg, frase_base_arg, respuesta_usuario_arg, descripcion_usuario_arg)

    else:
        # --- Modo Interactivo ---
        print("▶️  Modo interactivo iniciado.")
        while True:
            instance_id_arg = input("🆔 Introduce el ID de la instancia (ej. 1): ").strip()
            if instance_id_arg.isdigit():
                break
            else:
                print("❌ Por favor, introduce un número válido.")
        
        frase_base_arg = input("\nIntroduce la frase base para generar consultas: ")
        if not frase_base_arg:
            print("❌ No se introdujo ninguna frase. Saliendo.")
            sys.exit(1)
            
        respuesta_usuario_arg = input(f"\n💬 Introduce la respuesta: ").strip() or "Respuesta faltante"
        # Usar la frase base como descripción por defecto si no se provee una
        descripcion_usuario_arg = input(f"\n📝 Introduce la descripción (dejar en blanco usa la frase base): ").strip() or frase_base_arg
        
        ejecutar_generacion(instance_id_arg, frase_base_arg, respuesta_usuario_arg, descripcion_usuario_arg)

    input("\nPresiona Enter para salir...")
