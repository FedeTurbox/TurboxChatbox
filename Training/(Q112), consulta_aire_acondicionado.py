# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre aire acondicionado
frases_base = [
    "¿hay aire acondicionado?",
    "quiero saber si tienen aire acondicionado",
    "¿el hotel ofrece aire acondicionado?",
    "¿tienen aire en las habitaciones?",
    "quiero consultar por el aire acondicionado",
    "¿hay aire acondicionado disponible?",
    "¿puedo usar el aire acondicionado?",
    "¿ofrecen habitaciones con aire?",
    "¿el aire acondicionado está incluido?",
    "quiero saber si hay aire acondicionado en la habitación",
    "¿hay aire para los huéspedes?",
    "¿el hotel cuenta con aire acondicionado?",
    "¿tienen aire acondicionado para uso personal?",
    "quiero saber si puedo usar el aire acondicionado",
    "¿hay aire acondicionado en todas las habitaciones?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el aire acondicionado", "el aire", "aire acondicionado disponible"]

# Errores comunes
errores_comunes = {
    "aire": ["aire", "ayre", "aire"],
    "acondicionado": ["acondicionado", "acondisionado", "acondisionado"],
    "hotel": ["hotel", "hottel", "hotel"],
    "habitación": ["habitacion", "habitación", "habítacion"]
}

nombre_base = "consulta_aire_acondicionado"
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
