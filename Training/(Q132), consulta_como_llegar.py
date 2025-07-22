# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre cómo llegar / indicaciones
frases_base = [
    "¿cómo llego al hotel?",
    "quiero saber cómo llegar",
    "¿me pueden dar indicaciones para llegar?",
    "¿cómo se llega al hotel?",
    "quiero consultar por la ubicación y cómo llegar",
    "¿me pueden explicar cómo llegar al hotel?",
    "¿dónde está ubicado el hotel?",
    "quiero saber la dirección y cómo llegar",
    "¿pueden darme indicaciones para llegar?",
    "¿cómo llego desde el aeropuerto al hotel?",
    "quiero saber cómo llegar en transporte público",
    "¿me pueden dar rutas para llegar al hotel?",
    "¿cuál es la mejor forma de llegar al hotel?",
    "quiero consultar la ubicación exacta del hotel",
    "¿cómo llegar al hotel desde la ciudad?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "al hotel", "a la dirección", "a la ubicación"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "la ubicación", "las indicaciones", "la dirección"]

# Errores comunes
errores_comunes = {
    "llegar": ["llegar", "llegrar", "llegarr"],
    "hotel": ["hotel", "hottel", "hotel"],
    "dirección": ["direccion", "dirección", "direcion"],
    "ubicación": ["ubicacion", "ubicación", "ubicaciòn"]
}

nombre_base = "consulta_como_llegar"
n_perfectas = 200

# Generar frases
generar_con_errores(
    frases_base=frases_base,
    errores_comunes=errores_comunes,
    nombre_base=nombre_base,
    n_perfectas=n_perfectas,
    verbos=verbos,
    adverbios=adverbios,
    acciones=acciones,
    objetos=objetos
)
