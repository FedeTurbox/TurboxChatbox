# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para consultas de tipos de habitación
frases_base = [
    "quiero consultar por una habitación doble",
    "me gustaría preguntar por una habitación matrimonial",
    "deseo saber si hay habitaciones deluxe disponibles",
    "quiero información sobre las suites",
    "quiero consultar disponibilidad de habitaciones dobles",
    "quiero preguntar si hay suites libres",
    "quiero saber si hay habitaciones matrimoniales disponibles",
    "me gustaría consultar por una habitación deluxe",
    "quiero averiguar sobre las suites disponibles",
    "quiero preguntar por la disponibilidad de habitaciones dobles",
    "me interesa consultar sobre una habitación matrimonial",
    "quiero información sobre habitaciones deluxe",
    "quiero preguntar por una suite",
    "quiero saber si hay suites disponibles",
    "quiero consultar si puedo reservar una habitación doble",
    "quiero consultar por una habitación nupcial",
    "me gustaría preguntar por una habitación nupcial",
    "quiero saber si hay habitaciones nupciales disponibles"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "para esta fecha", "para el fin de semana", "para mañana"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "una habitación doble", "una habitación matrimonial", "una habitación deluxe", "una suite", "una habitación nupcial"]

# Errores comunes
errores_comunes = {
    "doble": ["doble", "doble", "doblle"],
    "matrimonial": ["matrimonial", "matrmonial", "matrimonal"],
    "deluxe": ["deluxe", "deluxe", "deluks"],
    "suite": ["suite", "suíte", "suite"],
    "nupcial": ["nupcial", "nupcial", "nupcial"],
    "habitación": ["habitacion", "habitación", "habítacion"],
    "consultar": ["consultar", "conultar", "consultar"],
    "disponibilidad": ["disponivilidad", "disponibilidad", "disponibildad"]
}

nombre_base = "consulta_tipo_habitacion"
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
