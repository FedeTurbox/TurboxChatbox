# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base
frases_base = [
    "hola",
    "buen dia",
    "buenos dias",
    "buenas tardes",
    "buenas noches",
    "hola buen dia",
    "hola buenos dias",
    "hola buenas tardes",
    "hola buenas noches",
    "que tal",
    "como esta",
    "como le va",
    "buenas",
    "muy buenas",
    "saludos"
]

# Componentes dinamicos
verbos = ["", "quisiera", "me gustaria", "podria", "puede"]
adverbios = ["", "por favor", "si es posible", "cuando pueda"]
acciones = ["saber", "consultar", "preguntar"]
objetos = ["algo", "una informacion", "un dato"]

# Errores comunes
errores_comunes = {
    "hola": ["ola", "jola", "holaa"],
    "buenos": ["buenoz", "buenoz", "bvenos"],
    "dias": ["dias", "dias", "días"],
    "tardes": ["tardez", "tardess", "tardes"],
    "noches": ["nochess", "nohez", "noxes"],
    "saludos": ["saludoz", "saludoss", "zaludos"],
    "como": ["komo", "cmomo", "cmo"],
    "esta": ["esta", "está", "esta"],
    "va": ["ba", "vah", "va"]
}

nombre_base = "saludo_usuario"
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
