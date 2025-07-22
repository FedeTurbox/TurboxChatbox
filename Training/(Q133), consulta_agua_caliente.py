# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre agua caliente
frases_base = [
    "¿hay agua caliente en las habitaciones?",
    "quiero saber si hay agua caliente disponible",
    "¿el hotel ofrece agua caliente las 24 horas?",
    "¿las habitaciones cuentan con agua caliente?",
    "quiero consultar por el agua caliente",
    "¿hay agua caliente para ducharse?",
    "¿puedo usar agua caliente durante mi estadía?",
    "¿el agua caliente está incluida en la habitación?",
    "quiero saber si el suministro de agua caliente es constante",
    "¿hay agua caliente en los baños?",
    "¿el hotel garantiza agua caliente?",
    "¿puedo tomar una ducha con agua caliente?",
    "quiero consultar si el agua caliente tiene algún costo",
    "¿hay agua caliente en todas las habitaciones?",
    "¿ofrecen agua caliente para los huéspedes?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "durante la estadía", "en el hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el agua caliente", "el suministro de agua caliente", "agua caliente en las habitaciones"]

# Errores comunes
errores_comunes = {
    "agua": ["agua", "agúa", "agua"],
    "caliente": ["caliente", "caliente", "calientee"],
    "habitaciones": ["habitaciones", "abitaciones", "habitaciones"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_agua_caliente"
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
