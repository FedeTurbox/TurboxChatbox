# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre accesibilidad
frases_base = [
    "¿el hotel es accesible para personas con discapacidad?",
    "quiero saber si tienen accesibilidad para sillas de ruedas",
    "¿hay rampas o elevadores para personas con movilidad reducida?",
    "¿ofrecen facilidades para personas con discapacidad?",
    "quiero consultar por accesibilidad en el hotel",
    "¿las habitaciones son accesibles?",
    "¿hay baños adaptados para discapacitados?",
    "¿pueden facilitar acceso para personas con movilidad limitada?",
    "¿el hotel tiene servicios para personas con discapacidad?",
    "quiero saber si hay señalización para personas con discapacidad",
    "¿ofrecen habitaciones accesibles?",
    "¿hay estacionamiento para discapacitados?",
    "¿el hotel cuenta con accesos adaptados?",
    "quiero saber si puedo reservar una habitación accesible",
    "¿el hotel tiene facilidades de accesibilidad?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "durante la estadía", "en las instalaciones"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "la accesibilidad", "facilidades para discapacitados", "servicios para personas con discapacidad"]

# Errores comunes
errores_comunes = {
    "accesibilidad": ["accesibilidad", "asesibilidad", "accesivilidad"],
    "discapacidad": ["discapacidad", "discapaciddad", "discapacidad"],
    "hotel": ["hotel", "hottel", "hotel"],
    "facilidades": ["facilidades", "facilidades", "facilidades"]
}

nombre_base = "consulta_accesibilidad"
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
