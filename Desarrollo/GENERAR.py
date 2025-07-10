import json
import random
from collections import defaultdict

def generar_variaciones_recorridos(n_perfectas=100, n_aleatorias=1000, archivo_salida="recorridos.json"):
    # Componentes para variantes de "ofrecen recorridos turísticos"
    componentes = {
        "inicio": {
            "ofrecen": 5, "disponen de": 4, "cuentan con": 4,
            "hay": 3, "se puede": 2, "proporcionan": 3
        },
        "objeto": {
            "recorridos turísticos": 5, "visitas guiadas": 4,
            "guía turístico": 3, "excursiones": 4, "tours": 3
        },
        "cierre": {
            "?": 6, "??": 2, "...": 2, "": 3
        }
    }

    # Errores típicos en palabras y puntuación
    errores_palabras = {
        "ofrecen": ["ofresen", "offrecen"],
        "disponen": ["dispnen", "dispenen"],
        "cuentan": ["cuntan", "cuetan"],
        "recorridos": ["recoridos", "recorrdos"],
        "turísticos": ["turisticos", "tursiticos"],
        "guiadas": ["guadas", "guiads"],
        "excursiones": ["excurciones", "excurciones"]
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
        "{inicio} {objeto}{cierre}",
        "¿{inicio} {objeto}{cierre}",
        "{inicio} {objeto} {cierre}"
    ]

    perfectas = []
    contador_palabras = defaultdict(int)
    total_palabras = 0

    for _ in range(n_perfectas):
        estructura = random.choice(estructuras_perfectas)
        params = {
            "inicio": seleccionar_proporcional("inicio"),
            "objeto": seleccionar_proporcional("objeto"),
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
            "cierre": seleccionar_proporcional("cierre")
        }

        frase = f"{params['inicio']} {params['objeto']}{params['cierre']}".strip()

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
    generar_variaciones_recorridos()
