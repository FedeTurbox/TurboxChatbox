# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre servicio de lavandería / laundry
frases_base = [
    "¿ofrecen servicio de lavandería?",
    "quiero saber si hay laundry en el hotel",
    "¿el hotel tiene servicio de lavado de ropa?",
    "¿tienen lavandería para los huéspedes?",
    "quiero consultar por el servicio de lavandería",
    "¿hay laundry disponible?",
    "¿puedo usar el servicio de lavandería?",
    "¿ofrecen lavado de ropa en el hotel?",
    "¿el servicio de lavandería tiene costo adicional?",
    "quiero saber si hay lavandería incluida en la estadía",
    "¿tienen servicio de ropa para los huéspedes?",
    "¿el hotel cuenta con laundry?",
    "¿hay lavandería las 24 horas?",
    "quiero saber si puedo solicitar lavado de ropa",
    "¿el servicio de laundry está disponible?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "durante la estadía", "para la ropa"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el servicio de lavandería", "el laundry", "lavado de ropa"]

# Errores comunes
errores_comunes = {
    "lavandería": ["lavanderia", "lavandería", "lavandería"],
    "laundry": ["laundry", "laundri", "laundry"],
    "ropa": ["ropa", "roppa", "ropa"],
    "servicio": ["servicio", "servisio", "servicio"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_lavanderia"
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
