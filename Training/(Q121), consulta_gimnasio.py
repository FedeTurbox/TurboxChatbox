# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre gimnasio
frases_base = [
    "¿hay gimnasio en el hotel?",
    "quiero saber si tienen gimnasio",
    "¿el hotel ofrece gimnasio para huéspedes?",
    "¿tienen sala de ejercicios o gimnasio?",
    "quiero consultar por el gimnasio",
    "¿hay gimnasio disponible para los huéspedes?",
    "¿puedo usar el gimnasio durante mi estadía?",
    "¿ofrecen gimnasio en las instalaciones?",
    "¿el gimnasio está abierto todo el día?",
    "quiero saber si hay gimnasio incluido",
    "¿tienen gimnasio las 24 horas?",
    "¿el hotel cuenta con gimnasio propio?",
    "¿hay equipo para hacer ejercicio?",
    "quiero saber si puedo usar la sala de ejercicios",
    "¿el gimnasio tiene costo adicional?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "durante la estadía", "en las instalaciones"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el gimnasio", "la sala de ejercicios", "el gimnasio del hotel"]

# Errores comunes
errores_comunes = {
    "gimnasio": ["gimnasio", "gimnacio", "gymnasio"],
    "hotel": ["hotel", "hottel", "hotel"],
    "ejercicio": ["ejercicio", "exercicio", "ejerccio"]
}

nombre_base = "consulta_gimnasio"
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
