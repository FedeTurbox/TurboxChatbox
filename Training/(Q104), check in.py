# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre horario de check-out / salida
frases_base = [
    "¿a qué hora es el check-out?",
    "quiero saber a qué hora debo salir",
    "¿cuándo es la salida del hotel?",
    "¿a qué hora puedo hacer el check-out?",
    "quiero consultar el horario de salida",
    "¿cuándo tengo que dejar la habitación?",
    "quiero saber el horario de check-out",
    "¿a qué hora termina el check-out?",
    "¿cuál es la hora de salida?",
    "¿a qué hora debo dejar la habitación?",
    "quiero saber cuándo es el check-out",
    "¿cuándo debo hacer la salida?",
    "¿a qué hora es la salida del hotel?",
    "¿a qué hora termina la estadía?",
    "quiero consultar la hora de check-out"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "para mi salida", "para hoy", "para mañana"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el check-out", "la salida", "la devolución de la habitación"]

# Errores comunes
errores_comunes = {
    "check-out": ["checkout", "chekout", "check-out"],
    "salida": ["salida", "salída", "salida"],
    "hora": ["hora", "ora", "hora"],
    "cuándo": ["cuando", "cuándo", "cuando"],
    "dejar": ["dejar", "dejjar", "dejar"]
}

nombre_base = "consulta_horario_checkout"
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
