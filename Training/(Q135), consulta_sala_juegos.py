# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre sala de juegos y actividades para niños
frases_base = [
    "¿hay sala de juegos en el hotel?",
    "quiero saber si tienen actividades para niños",
    "¿ofrecen actividades infantiles?",
    "¿hay lugar para que jueguen los niños?",
    "quiero consultar por la sala de juegos",
    "¿tienen juegos para niños en el hotel?",
    "¿ofrecen actividades recreativas para niños?",
    "¿hay espacio para juegos infantiles?",
    "quiero saber si hay entretenimiento para los más pequeños",
    "¿el hotel cuenta con sala de juegos?",
    "¿hay actividades infantiles durante la estadía?",
    "¿ofrecen juegos y actividades para niños?",
    "¿hay área de juegos para los niños?",
    "quiero consultar si tienen actividades para niños",
    "¿ofrecen sala de juegos y actividades infantiles?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "durante la estadía", "en las instalaciones"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "la sala de juegos", "actividades para niños", "actividades infantiles", "juegos para niños"]

# Errores comunes
errores_comunes = {
    "juegos": ["juegos", "juegoss", "juejos"],
    "niños": ["niños", "niñoss", "niños"],
    "actividades": ["actividades", "actividaddes", "actividades"],
    "infantiles": ["infantiles", "infantilless", "infantiles"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_sala_juegos"
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
