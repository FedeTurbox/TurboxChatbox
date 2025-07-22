# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base
frases_base = [
    "donde esta el lugar",
    "donde queda",
    "cual es la direccion",
    "me puede decir donde esta",
    "podria darme la ubicacion",
    "donde esta ubicado",
    "en que calle esta",
    "cual es la ubicacion exacta",
    "puede indicarme la direccion",
    "necesito saber donde esta",
    "podria decirme la direccion",
    "podria decirme donde queda",
    "me podria decir la direccion",
    "me podria decir donde queda",
    "seria tan amable de decirme la ubicacion",
    "seria tan amable de decirme donde esta"
]

# Componentes dinamicos
verbos = ["", "puedo", "podria", "me podria", "seria tan amable de"]
adverbios = ["", "por favor", "ahora", "rapidamente"]
acciones = ["saber", "consultar", "preguntar", "decirme", "darme"]
objetos = ["la direccion", "la ubicacion", "el lugar exacto", "el sitio"]

# Errores comunes
errores_comunes = {
    "donde": ["donnde", "dnde", "dodne"],
    "direccion": ["direcion", "dirreccion", "direxion"],
    "ubicacion": ["ubikacion", "ubicazion", "ubicasion"],
    "queda": ["qeda", "keda", "queda"],
    "calle": ["calle", "callee", "kalle"],
    "decirme": ["decir me", "dezirme", "desirme"],
    "amable": ["amabre", "hamable"]
}

nombre_base = "pregunta_ubicacion"
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
