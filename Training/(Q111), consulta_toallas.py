# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre toallas
frases_base = [
    "¿hay toallas disponibles?",
    "quiero saber si tienen toallas",
    "¿el hotel ofrece toallas?",
    "¿tienen toallas para los huéspedes?",
    "quiero consultar por las toallas",
    "¿hay toallas en la habitación?",
    "¿puedo usar toallas?",
    "¿ofrecen toallas limpias?",
    "¿las toallas están incluidas?",
    "quiero saber si hay toallas disponibles",
    "¿hay toallas suficientes?",
    "¿el hotel cuenta con toallas?",
    "¿tienen toallas para uso personal?",
    "quiero saber si puedo usar toallas",
    "¿hay toallas limpias disponibles?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "las toallas", "toallas limpias", "toallas disponibles"]

# Errores comunes
errores_comunes = {
    "toallas": ["toallas", "toallas", "toallas"],
    "hotel": ["hotel", "hotel", "hottel"],
    "habitación": ["habitacion", "habitación", "habítacion"],
    "disponibles": ["disponibles", "disponiblles", "disponibles"]
}

nombre_base = "consulta_toallas"
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
