# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base
frases_base = [
    "cual es el numero de telefono",
    "cual es el numero telefonico",
    "puede darme el telefono",
    "puede darme el numero telefonico",
    "me puede dar el numero",
    "me puede dar el numero telefonico",
    "podria decirme el telefono",
    "podria decirme el numero telefonico",
    "me podria dar el contacto",
    "necesito el numero de contacto",
    "necesito el numero telefonico",
    "puede indicarme el telefono",
    "puede indicarme el numero telefonico",
    "quiero saber el numero",
    "quiero saber el numero telefonico",
    "podria darme el telefono",
    "cual es el telefono de contacto",
    "cual es el numero telefonico de contacto",
    "me da el numero",
    "me puede facilitar el telefono",
    "me puede facilitar el numero telefonico",
    "seria tan amable de darme el numero",
    "seria tan amable de darme el numero telefonico",
    "necesito saber el telefono",
    "necesito saber el numero telefonico",
    "puede decirme el numero"
]

# Componentes dinamicos
verbos = ["", "podria", "puede", "me podria", "quisiera"]
adverbios = ["", "por favor", "ahora", "cuando pueda"]
acciones = ["darme", "facilitarme", "indicarme", "decirme", "proporcionarme"]
objetos = [
    "el telefono",
    "el numero de telefono",
    "el numero telefonico",
    "el numero de contacto",
    "el contacto",
    "el telefono de contacto",
    "el numero telefonico de contacto"
]

# Errores comunes
errores_comunes = {
    "telefono": ["telefóno", "telefoono", "telefno", "teléfono"],
    "telefonico": ["telefónico", "telefoniko", "telefonico", "telefóniko"],
    "numero": ["numro", "número", "numéro", "numro"],
    "contacto": ["contactto", "kontacto", "contacot"],
    "darme": ["darmme", "dárme", "dar me"],
    "decirme": ["dezirme", "desirme", "decir me"],
    "facilitarme": ["facilitarme", "fasilitarme", "facilitarmme"]
}

nombre_base = "pregunta_telefono"
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
