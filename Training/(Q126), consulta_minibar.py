# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre minibar
frases_base = [
    "¿la habitación tiene minibar?",
    "quiero saber si hay minibar disponible",
    "¿ofrecen minibar en las habitaciones?",
    "¿las habitaciones cuentan con minibar?",
    "quiero consultar por el minibar",
    "¿hay minibar para los huéspedes?",
    "¿puedo usar el minibar durante mi estadía?",
    "¿el minibar está incluido en la habitación?",
    "quiero saber si el minibar tiene costo adicional",
    "¿el hotel ofrece minibar en las habitaciones?",
    "¿hay bebidas disponibles en el minibar?",
    "¿el minibar está surtido en la habitación?",
    "¿puedo acceder al minibar cuando quiera?",
    "quiero consultar si el minibar está disponible",
    "¿ofrecen minibar en las habitaciones del hotel?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "durante la estadía", "en el hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el minibar", "bebidas del minibar", "minibar en la habitación"]

# Errores comunes
errores_comunes = {
    "minibar": ["minibar", "minbar", "minibar"],
    "habitación": ["habitacion", "habitación", "habítacion"],
    "hotel": ["hotel", "hottel", "hotel"],
    "bebidas": ["bebidas", "bebidas", "bebidass"]
}

nombre_base = "consulta_minibar"
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
