# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre ascensores
frases_base = [
    "¿el hotel tiene ascensor?",
    "quiero saber si hay ascensores disponibles",
    "¿las habitaciones son accesibles por ascensor?",
    "¿ofrecen ascensor para los huéspedes?",
    "quiero consultar por los ascensores del hotel",
    "¿hay ascensores en el edificio?",
    "¿puedo usar el ascensor durante mi estadía?",
    "¿el ascensor está funcionando?",
    "quiero saber si hay ascensores las 24 horas",
    "¿tienen ascensor para subir a las habitaciones?",
    "¿el hotel cuenta con ascensores modernos?",
    "¿hay ascensor para personas con movilidad reducida?",
    "quiero consultar si el ascensor está disponible",
    "¿ofrecen ascensores para todos los pisos?",
    "¿hay ascensor para uso de los huéspedes?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "durante la estadía", "en el edificio"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el ascensor", "los ascensores", "el elevador"]

# Errores comunes
errores_comunes = {
    "ascensor": ["ascensor", "asensor", "ascensoor"],
    "hotel": ["hotel", "hottel", "hotel"],
    "habitaciones": ["habitaciones", "abitaciones", "habitaciones"]
}

nombre_base = "consulta_ascensor"
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
