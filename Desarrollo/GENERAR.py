import json
import random
from collections import defaultdict

def generar_variaciones_pregunta(n_perfectas=100, n_aleatorias=1000, archivo_salida="preguntas.json"):
    # Componentes para variantes de "tengo una pregunta"
    componentes = {
        "inicio": {
            "tengo": 5, "me surge": 3, "quisiera hacer": 3,
            "quería": 4, "puedo hacer": 3, "hay": 2, "necesito hacer": 2
        },
        "objeto": {
            "una pregunta": 5, "una duda": 4, "una consulta": 4,
            "un comentario": 2, "algo que preguntar": 2
        },
        "extra": {
            "rápida": 2, "importante": 2, "": 6
        },
        "cierre": {
            "?": 5, "??": 2, "...": 2, "": 3
        }
    }

    # Errores típicos en palabras y puntuación
    errores_palabras = {
        "tengo": ["tngo", "tnego"],
        "pregunta": ["pregnta", "preguta"],
        "duda": ["ddua", "duada"],
        "consulta": ["consuta", "consulata"]
    }
    errores_puntuacion = ["??", "...", "?!", ".", ""]

    # Preparar selección ponderada
    componentes_ponderados = {
        categoria: list(palabras.keys())
        for categoria, palabras in componentes.items()
    }
    pesos = {
        categoria: list(palabras.values())
        for categoria, palabras in componentes.items()
    }

    def seleccionar_proporcional(categoria):
        return random.choices(
            componentes_ponderados[categoria],
            weights=pesos[categoria],
            k=1
        )[0]

    estructuras_perfectas = [
        "{inicio} {objeto} {extra}{cierre}",
        "{inicio} {objeto}{cierre}",
        "{inicio} {objeto} {extra}{cierre}"
    ]

    perfectas = []
    contador_palabras = defaultdict(int)
    total_palabras = 0

    for _ in range(n_perfectas):
        estructura = random.choice(estructuras_perfectas)
        params = {
            "inicio": seleccionar_proporcional("inicio"),
            "objeto": seleccionar_proporcional("objeto"),
            "extra": seleccionar_proporcional("extra"),
            "cierre": seleccionar_proporcional("cierre")
        }

        frase = estructura.format(**params).strip().capitalize()
        perfectas.append(frase)

        # Actualizar contadores
        for palabra in params.values():
            contador_palabras[palabra] += 1
            total_palabras += 1

    # Variaciones aleatorias con errores
    aleatorias = []
    for _ in range(n_aleatorias):
        params = {
            "inicio": seleccionar_proporcional("inicio"),
            "objeto": seleccionar_proporcional("objeto"),
            "extra": seleccionar_proporcional("extra"),
            "cierre": seleccionar_proporcional("cierre")
        }

        frase = f"{params['inicio']} {params['objeto']} {params['extra']}{params['cierre']}".strip()

        # Aplicar errores en palabras
        if random.random() < 0.3:
            for palabra, alternativas in errores_palabras.items():
                if palabra in frase and random.random() < 0.5:
                    frase = frase.replace(palabra, random.choice(alternativas), 1)

        # Aplicar errores de puntuación
        if random.random() < 0.3:
            if params['cierre'] in ["?", ".", "?!"]:
                frase = frase.rstrip(params['cierre'])
                frase += random.choice(errores_puntuacion)

        if random.random() < 0.5:
            frase = frase.capitalize()

        aleatorias.append(frase)

        # Actualizar contadores
        for palabra in params.values():
            contador_palabras[palabra] += 1
            total_palabras += 1

    # Guardar resultados
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump({
            "perfectas": perfectas,
            "con_errores": aleatorias,
            "total": len(perfectas) + len(aleatorias),
            "distribucion": {k: v/total_palabras for k, v in contador_palabras.items()}
        }, f, ensure_ascii=False, indent=2)

    print(f"✅ Generadas {len(perfectas)} variaciones perfectas y {len(aleatorias)} aleatorias")
    print("Distribución aproximada de palabras:")
    for cat, palabras in componentes.items():
        print(f"\n{cat.capitalize()}:")
        for pal, peso in palabras.items():
            uso = contador_palabras.get(pal, 0)/total_palabras
            print(f"  {pal}: Esperado {peso/sum(palabras.values()):.1%}, Actual {uso:.1%}")

if __name__ == "__main__":
    generar_variaciones_pregunta()
