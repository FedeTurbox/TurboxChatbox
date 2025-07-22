# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre servicio a la habitación / room service
frases_base = [
    "¿hay servicio a la habitación?",
    "quiero saber si ofrecen room service",
    "¿el hotel tiene servicio a la habitación?",
    "¿tienen servicio de comida en la habitación?",
    "quiero consultar por el servicio a la habitación",
    "¿hay room service disponible?",
    "¿puedo pedir servicio a la habitación?",
    "¿ofrecen comida en la habitación?",
    "¿el servicio a la habitación tiene costo adicional?",
    "quiero saber si hay room service incluido",
    "¿tienen servicio a la habitación para huéspedes?",
    "¿el hotel ofrece servicio de habitaciones?",
    "¿hay servicio a la habitación las 24 horas?",
    "quiero saber si puedo solicitar room service",
    "¿el servicio de habitación está incluido en la reserva?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el servicio a la habitación", "el room service", "servicio de comida en la habitación"]

# Errores comunes
errores_comunes = {
    "servicio": ["servicio", "servisio", "servisio"],
    "habitación": ["habitacion", "habitación", "habítacion"],
    "room service": ["room service", "rum servis", "roomservice"],
    "comida": ["comida", "comidda", "comyda"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_servicio_habitacion"
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
