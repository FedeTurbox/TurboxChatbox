# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre escritorio para trabajar
frases_base = [
    "¿la habitación tiene escritorio para trabajar?",
    "quiero saber si hay un escritorio disponible",
    "¿ofrecen escritorio en la habitación?",
    "¿las habitaciones cuentan con espacio para trabajar?",
    "quiero consultar por un escritorio para usar",
    "¿hay escritorio en las habitaciones?",
    "¿puedo trabajar en la habitación con un escritorio?",
    "¿ofrecen espacio para trabajar en la habitación?",
    "quiero saber si puedo usar un escritorio durante la estadía",
    "¿las habitaciones tienen escritorio propio?",
    "¿hay un escritorio adecuado para trabajar?",
    "¿el hotel proporciona escritorio en la habitación?",
    "¿puedo reservar habitación con escritorio?",
    "quiero consultar si hay espacio para trabajar",
    "¿ofrecen escritorio para huéspedes?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "durante la estadía", "en el hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el escritorio", "espacio para trabajar", "escritorio en la habitación"]

# Errores comunes
errores_comunes = {
    "escritorio": ["escritorio", "escritorio", "escritorio"],
    "trabajar": ["trabajar", "trabahar", "trabajar"],
    "habitación": ["habitacion", "habitación", "habítacion"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_escritorio_trabajo"
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
