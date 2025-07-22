# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para consultas de habitación, pieza, cama, lugar, etc.
frases_base = [
    "quiero consultar por una habitación",
    "me gustaría preguntar por una pieza",
    "deseo saber si hay camas disponibles",
    "quiero información sobre un lugar",
    "quiero consultar disponibilidad de habitación",
    "quiero preguntar si hay lugar",
    "quiero saber si hay piezas libres",
    "me gustaría consultar por una cama",
    "quiero averiguar sobre habitaciones",
    "quiero preguntar por la disponibilidad",
    "me interesa consultar sobre una pieza",
    "quiero información sobre camas disponibles",
    "quiero preguntar por un lugar en el hotel",
    "quiero saber si hay espacio libre",
    "quiero consultar si puedo reservar una habitación"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "para esta fecha", "para el fin de semana", "para mañana"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "una habitación", "una pieza", "una cama", "un lugar"]

# Errores comunes
errores_comunes = {
    "habitación": ["abitación", "habitaion", "habitación"],
    "pieza": ["pieza", "piesa", "pieza"],
    "cama": ["cama", "kama", "cama"],
    "lugar": ["lugar", "luhgar", "lugar"],
    "consultar": ["consultar", "conultar", "consultar"],
    "preguntar": ["preguntar", "prejuntar", "preguntar"],
    "disponibilidad": ["disponivilidad", "disponibilidad", "disponibildad"]
}

nombre_base = "consulta_pieza_usuario"
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
