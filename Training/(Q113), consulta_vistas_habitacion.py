# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre vistas de las habitaciones
frases_base = [
    "¿las habitaciones tienen vista a la calle?",
    "quiero saber si hay habitaciones con buenas vistas",
    "¿el hotel ofrece vistas panorámicas?",
    "¿hay habitaciones con vista a paisajes?",
    "quiero consultar si hay habitaciones con vista al exterior",
    "¿las habitaciones tienen vista a la ciudad?",
    "¿puedo reservar habitación con vistas?",
    "¿hay habitaciones con vista al mar?",
    "quiero saber si hay vistas panorámicas",
    "¿hay habitaciones con vista a la montaña?",
    "¿el hotel tiene habitaciones con vista al jardín?",
    "¿puedo elegir habitación con buenas vistas?",
    "quiero consultar por habitaciones con vistas panorámicas",
    "¿hay habitaciones con vistas bonitas?",
    "¿las habitaciones tienen vista al paisaje?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "habitaciones con vista", "vistas panorámicas", "vista a paisajes"]

# Errores comunes
errores_comunes = {
    "vista": ["vista", "vysta", "vista"],
    "vistas": ["vistas", "vystas", "vistas"],
    "panorámicas": ["panoramicas", "panorámicas", "panoramícas"],
    "paisajes": ["paisajes", "paisajjes", "paisages"],
    "habitaciones": ["habitaciones", "avitaciones", "habitasiones"],
    "calle": ["calle", "calle", "calle"]
}

nombre_base = "consulta_vistas_habitacion"
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
