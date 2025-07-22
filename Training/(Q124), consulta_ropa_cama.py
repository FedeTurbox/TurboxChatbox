# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre ropa de cama
frases_base = [
    "¿la habitación incluye ropa de cama?",
    "quiero saber si hay ropa de cama disponible",
    "¿ofrecen ropa de cama limpia?",
    "¿las camas tienen sábanas y cobijas?",
    "quiero consultar por la ropa de cama",
    "¿hay ropa de cama para los huéspedes?",
    "¿proporcionan ropa de cama en las habitaciones?",
    "¿la ropa de cama está incluida en la reserva?",
    "quiero saber si cambian la ropa de cama",
    "¿las habitaciones cuentan con ropa de cama limpia?",
    "¿hay sábanas y fundas en las camas?",
    "¿ofrecen cambio de ropa de cama durante la estadía?",
    "¿la habitación tiene ropa de cama adecuada?",
    "quiero consultar si la ropa de cama es de calidad",
    "¿proporcionan ropa de cama para todos los huéspedes?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "durante la estadía", "en el hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "la ropa de cama", "las sábanas", "las fundas"]

# Errores comunes
errores_comunes = {
    "ropa": ["ropa", "roppa", "ropa"],
    "cama": ["cama", "camma", "cama"],
    "sábanas": ["sabanas", "sábanas", "sabannas"],
    "fundas": ["fundas", "fundass", "fundas"],
    "habitación": ["habitacion", "habitación", "habítacion"]
}

nombre_base = "consulta_ropa_cama"
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
