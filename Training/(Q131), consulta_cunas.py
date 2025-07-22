# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre cunas
frases_base = [
    "¿el hotel tiene cunas disponibles?",
    "quiero saber si ofrecen cunas para bebés",
    "¿hay cunas para los niños pequeños?",
    "¿pueden proporcionar una cuna en la habitación?",
    "quiero consultar por las cunas del hotel",
    "¿hay cunas disponibles para huéspedes con bebés?",
    "¿ofrecen cunas durante la estadía?",
    "¿puedo solicitar una cuna para mi bebé?",
    "¿las habitaciones cuentan con cunas?",
    "quiero saber si hay cunas para niños pequeños",
    "¿el hotel proporciona cunas para bebés?",
    "¿puedo reservar con cuna incluida?",
    "¿hay cunas para bebés disponibles en el hotel?",
    "quiero consultar si las cunas tienen costo adicional",
    "¿ofrecen cunas para huéspedes con bebés?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "durante la estadía", "en el hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "las cunas", "la cuna para bebés", "cunas disponibles"]

# Errores comunes
errores_comunes = {
    "cunas": ["cunas", "cunnas", "cunas"],
    "bebés": ["bebes", "bebés", "bebes"],
    "hotel": ["hotel", "hottel", "hotel"],
    "habitacion": ["habitacion", "habitación", "habítacion"]
}

nombre_base = "consulta_cunas"
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
