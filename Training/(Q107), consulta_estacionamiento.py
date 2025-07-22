# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre estacionamiento
frases_base = [
    "¿tienen estacionamiento?",
    "quiero saber si hay lugar para estacionar",
    "¿ofrecen parking para huéspedes?",
    "¿hay estacionamiento disponible?",
    "¿cuánto cuesta el estacionamiento?",
    "quiero consultar por el estacionamiento",
    "¿el estacionamiento está incluido?",
    "¿hay espacio para dejar el auto?",
    "¿tienen cochera para autos?",
    "quiero saber si el parking es gratis",
    "¿el estacionamiento tiene costo adicional?",
    "¿ofrecen lugar para estacionar el vehículo?",
    "¿hay estacionamiento privado?",
    "quiero saber si puedo dejar mi auto allí",
    "¿el hotel cuenta con estacionamiento?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "en las instalaciones", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el estacionamiento", "el parking", "la cochera"]

# Errores comunes
errores_comunes = {
    "estacionamiento": ["estasionamiento", "estacionamiento", "estacionamineto"],
    "parking": ["parking", "parkin", "parking"],
    "cochera": ["cochera", "cohera", "cochera"],
    "auto": ["auto", "auto", "auto"],
    "costo": ["costo", "costó", "costo"],
    "incluido": ["incluido", "incluido", "incluio"]
}

nombre_base = "consulta_estacionamiento"
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
