# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base
frases_base = [
    "gracias",
    "muchas gracias",
    "mil gracias",
    "le agradezco",
    "muchisimas gracias",
    "gracias por la ayuda",
    "gracias por su tiempo",
    "le estoy agradecido",
    "estoy muy agradecido",
    "gracias de antemano",
    "muchas gracias por todo",
    "le agradezco mucho",
    "muchas gracias por la informacion",
    "gracias por responder",
    "gracias por atenderme"
]

# Componentes dinamicos
verbos = ["", "le agradezco", "quiero agradecerle", "estoy agradecido"]
adverbios = ["", "mucho", "de corazón", "de verdad", "sinceramente"]
acciones = ["la ayuda", "el apoyo", "su tiempo", "la informacion", "su atencion"]
objetos = ["", "que me brindo", "que me dio", "que me ofrecio"]

# Errores comunes
errores_comunes = {
    "gracias": ["grasias", "gracis", "gracias"],
    "muchas": ["muhas", "mucas", "muchaz"],
    "mil": ["mil", "mil", "míl"],
    "ayuda": ["ayda", "aiuda", "aydua"],
    "informacion": ["informasion", "informazion", "infornacion"],
    "atencion": ["atencion", "atenssion", "atenssión"],
    "agradezco": ["agradesco", "agredezco", "agradesko"]
}

nombre_base = "agradecimiento_usuario"
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
