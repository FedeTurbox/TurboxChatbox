# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre desayuno
frases_base = [
    "¿el desayuno está incluido?",
    "quiero saber si el desayuno tiene costo",
    "¿el desayuno es gratis?",
    "¿incluye desayuno la reserva?",
    "¿hay desayuno incluido?",
    "quiero consultar si el desayuno está incluido",
    "¿tengo que pagar por el desayuno?",
    "¿cuánto cuesta el desayuno?",
    "¿el desayuno está disponible?",
    "¿el desayuno está incluido en el precio?",
    "¿el desayuno tiene algún costo adicional?",
    "quiero saber si el desayuno es gratuito",
    "¿se ofrece desayuno incluido?",
    "¿el desayuno es parte de la reserva?",
    "¿el desayuno tiene costo extra?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el desayuno", "la comida", "el desayuno incluido"]

# Errores comunes
errores_comunes = {
    "desayuno": ["desayno", "desayuuno", "desayuno"],
    "incluido": ["incluido", "incluido", "incluio"],
    "costo": ["costo", "costó", "costo"],
    "gratis": ["grátis", "gratis", "gratus"],
    "pagar": ["pagar", "pagaar", "pagar"],
    "precio": ["precio", "prezio", "precio"]
}

nombre_base = "consulta_desayuno"
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
