# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre menú especial
frases_base = [
    "¿tienen menú vegetariano?",
    "quiero saber si hay opciones para celíacos",
    "¿ofrecen menú sin gluten?",
    "¿hay menú para personas con alergias?",
    "¿tienen opciones vegetarianas?",
    "quiero consultar por el menú sin gluten",
    "¿ofrecen comida para celíacos?",
    "¿hay menú especial para dietas?",
    "quiero saber si tienen menú para alergias alimentarias",
    "¿ofrecen menú vegano o vegetariano?",
    "¿tienen opciones sin gluten?",
    "quiero consultar por opciones para celíacos",
    "¿ofrecen platos vegetarianos?",
    "¿tienen menú para personas con intolerancias?",
    "quiero saber si el menú incluye opciones especiales"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el restaurante", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el menú vegetariano", "opciones para celíacos", "menú sin gluten", "menú especial"]

# Errores comunes
errores_comunes = {
    "vegetariano": ["vegetariano", "vegetaríano", "vegetariano"],
    "celíaco": ["celiaco", "celíaco", "celiáco"],
    "gluten": ["gluten", "glutén", "gluten"],
    "menú": ["menu", "menú", "menu"],
    "alergias": ["alergias", "alergías", "alergias"],
    "intolerancias": ["intolerancias", "intoleráncias", "intolerancias"]
}

nombre_base = "consulta_menu_especial"
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
