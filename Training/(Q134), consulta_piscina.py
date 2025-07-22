# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre piscina
frases_base = [
    "¿hay piscina en el hotel?",
    "quiero saber si tienen piscina disponible",
    "¿el hotel ofrece piscina para huéspedes?",
    "¿tienen pileta en las instalaciones?",
    "quiero consultar por la piscina",
    "¿hay piscina climatizada?",
    "¿puedo usar la piscina durante mi estadía?",
    "¿la piscina está abierta todo el día?",
    "quiero saber si la piscina tiene costo adicional",
    "¿ofrecen piscina en el hotel?",
    "¿hay piscina para niños?",
    "¿el hotel cuenta con piscina al aire libre?",
    "¿hay piscina cubierta?",
    "quiero consultar si la piscina está disponible",
    "¿pueden darme información sobre la piscina?",
    "¿hay piscina techada?",
    "¿la piscina es climatizada?",
    "¿ofrecen piscina techada y climatizada?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "durante la estadía", "en las instalaciones"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "la piscina", "la pileta", "la piscina del hotel", "piscina climatizada", "piscina techada"]

# Errores comunes
errores_comunes = {
    "piscina": ["piscina", "pizcina", "piscinaa"],
    "hotel": ["hotel", "hottel", "hotel"],
    "pileta": ["pileta", "pilletta", "piletta"],
    "climatizada": ["climatizada", "climatizadda", "climatizada"],
    "techada": ["techada", "techaada", "techada"]
}

nombre_base = "consulta_piscina"
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
