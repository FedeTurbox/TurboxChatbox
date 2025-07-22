# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre TV por cable
frases_base = [
    "¿la habitación tiene TV por cable?",
    "quiero saber si ofrecen canales por cable",
    "¿hay cable en la televisión de la habitación?",
    "¿ofrecen señal de TV por cable?",
    "quiero consultar por la TV por cable",
    "¿la televisión incluye canales por cable?",
    "¿puedo ver canales por cable durante mi estadía?",
    "¿el hotel tiene televisión por cable?",
    "quiero saber si hay canales de cable disponibles",
    "¿la habitación cuenta con señal de cable?",
    "¿ofrecen paquetes de TV por cable?",
    "¿hay canales de cable en las habitaciones?",
    "quiero consultar si la TV es por cable",
    "¿puedo usar la TV por cable en la habitación?",
    "¿ofrecen cable en la televisión del hotel?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "durante la estadía", "en el hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "la TV por cable", "canales por cable", "señal de cable"]

# Errores comunes
errores_comunes = {
    "cable": ["cable", "cablee", "cabel"],
    "televisión": ["television", "televisión", "televison"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_cable_tv"
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
