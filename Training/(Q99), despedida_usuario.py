# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base
frases_base = [
    "adios",
    "hasta luego",
    "hasta pronto",
    "nos vemos",
    "hasta la proxima",
    "chau",
    "chao",
    "me despido",
    "que tenga buen dia",
    "que tenga buenas tardes",
    "que tenga buenas noches",
    "fue un gusto",
    "nos vemos pronto"
]

# Componentes dinamicos
verbos = ["", "me retiro", "me voy", "me despido"]
adverbios = ["", "por ahora", "entonces", "ya"]
acciones = ["", "agradeciendo", "saludando"]
objetos = ["", "por la atencion", "por la ayuda", "de nuevo"]

# Errores comunes
errores_comunes = {
    "adios": ["adiós", "adioss", "adiosz"],
    "chau": ["chao", "chaw", "chauu"],
    "hasta": ["asta", "hasta", "hsta"],
    "luego": ["lueggo", "lueego", "lueguo"],
    "pronto": ["pronto", "prontto", "pronto"],
    "proxima": ["proxíma", "proxma", "proxima"],
    "tenga": ["tenga", "tenga", "tenga"],
    "gusto": ["gusto", "gusto", "gustto"]
}

nombre_base = "despedida_usuario"
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
