# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre servicios de streaming
frases_base = [
    "¿la habitación tiene Netflix?",
    "quiero saber si ofrecen servicios de streaming",
    "¿puedo ver Disney Plus en la TV?",
    "¿hay acceso a HBO en las habitaciones?",
    "quiero consultar por Netflix y otros servicios de streaming",
    "¿tienen acceso a plataformas como Netflix o HBO?",
    "¿la smart TV tiene aplicaciones de streaming?",
    "¿puedo usar servicios como Disney Plus en la habitación?",
    "¿ofrecen canales de streaming en la televisión?",
    "quiero saber si hay acceso a Netflix o Disney Plus",
    "¿hay streaming disponible en la TV del hotel?",
    "¿la televisión incluye aplicaciones como HBO Max?",
    "¿puedo ver películas por streaming en la habitación?",
    "quiero consultar si hay acceso a plataformas de streaming",
    "¿el hotel ofrece Netflix, Disney Plus, HBO u otros servicios?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "durante la estadía", "en el hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "Netflix", "servicios de streaming", "Disney Plus", "HBO", "plataformas de streaming"]

# Errores comunes
errores_comunes = {
    "Netflix": ["Netflix", "Netflx", "Netfix"],
    "streaming": ["streaming", "straming", "streeming"],
    "Disney Plus": ["Disney Plus", "Diseny Plus", "DisneyPluss"],
    "HBO": ["HBO", "H.B.O", "HBOo"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_streaming"
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
