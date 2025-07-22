# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre admisión de niños
frases_base = [
    "¿el hotel admite niños?",
    "quiero saber si aceptan niños en las habitaciones",
    "¿puedo reservar con niños?",
    "¿aceptan niños durante la estadía?",
    "quiero consultar si hay restricciones para niños",
    "¿los niños pueden hospedarse en el hotel?",
    "¿aceptan menores en las habitaciones?",
    "¿hay políticas para la admisión de niños?",
    "¿pueden alojarse niños en las habitaciones?",
    "quiero saber si hay tarifas especiales para niños",
    "¿hay servicios para niños en el hotel?",
    "¿aceptan niños pequeños en el hotel?",
    "¿puedo hospedarme con mis hijos?",
    "quiero saber si admiten niños de todas las edades",
    "¿hay áreas especiales para niños?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "durante la estadía", "en las habitaciones"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "los niños", "menores", "niños y niñas", "menores de edad"]

# Errores comunes
errores_comunes = {
    "niños": ["niños", "niñoss", "niños"],
    "hotel": ["hotel", "hottel", "hotel"],
    "admiten": ["admiten", "admitenn", "adminten"],
    "menores": ["menores", "menores", "menorees"]
}

nombre_base = "consulta_admision_ninos"
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
