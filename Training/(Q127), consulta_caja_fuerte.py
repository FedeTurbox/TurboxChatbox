# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre caja fuerte
frases_base = [
    "¿la habitación tiene caja fuerte?",
    "quiero saber si hay caja fuerte disponible",
    "¿ofrecen caja fuerte en las habitaciones?",
    "¿las habitaciones cuentan con caja fuerte?",
    "quiero consultar por la caja fuerte",
    "¿hay caja fuerte para los huéspedes?",
    "¿puedo usar la caja fuerte durante mi estadía?",
    "¿la caja fuerte está incluida en la habitación?",
    "quiero saber si la caja fuerte tiene costo adicional",
    "¿el hotel ofrece caja fuerte en las habitaciones?",
    "¿hay lugar seguro para guardar objetos de valor?",
    "¿la habitación tiene caja de seguridad?",
    "¿puedo acceder a la caja fuerte cuando quiera?",
    "quiero consultar si la caja fuerte está disponible",
    "¿ofrecen caja fuerte para guardar mis pertenencias?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "durante la estadía", "en el hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "la caja fuerte", "la caja de seguridad", "el lugar seguro"]

# Errores comunes
errores_comunes = {
    "caja fuerte": ["caja fuerte", "caja fuert", "caja fuerte"],
    "habitación": ["habitacion", "habitación", "habítacion"],
    "hotel": ["hotel", "hottel", "hotel"],
    "seguridad": ["seguridad", "seguriddad", "seguridad"]
}

nombre_base = "consulta_caja_fuerte"
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
