# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre horario de check-in / ingreso
frases_base = [
    "¿a qué hora es el check-in?",
    "quiero saber a qué hora puedo ingresar",
    "¿cuándo es el ingreso al hotel?",
    "¿a qué hora puedo hacer el check-in?",
    "quiero consultar el horario de ingreso",
    "¿cuándo puedo entrar a la habitación?",
    "quiero saber el horario de check-in",
    "¿a qué hora empieza el check-in?",
    "¿cuál es la hora de ingreso?",
    "¿a qué hora abren para el check-in?",
    "quiero saber cuándo puedo ingresar",
    "¿cuándo comienza el ingreso?",
    "¿a qué hora puedo entrar al hotel?",
    "¿a qué hora es la entrada?",
    "quiero consultar la hora de check-in"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "para mi llegada", "para hoy", "para mañana"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el check-in", "el ingreso", "la entrada"]

# Errores comunes
errores_comunes = {
    "check-in": ["checkin", "chekin", "check-in"],
    "ingreso": ["ingreso", "inreso", "ingreso"],
    "hora": ["hora", "ora", "hora"],
    "cuándo": ["cuando", "cuándo", "cuando"],
    "entrada": ["entrada", "entrda", "entrada"]
}

nombre_base = "consulta_horario_checkin"
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
