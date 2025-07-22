# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre spa, masajes y bienestar
frases_base = [
    "¿el hotel tiene spa?",
    "quiero saber si ofrecen masajes",
    "¿hay centro de bienestar en el hotel?",
    "¿tienen servicio de spa para huéspedes?",
    "quiero consultar por masajes y tratamientos",
    "¿puedo reservar masajes en el hotel?",
    "¿ofrecen terapias de relajación o spa?",
    "¿hay masajes disponibles durante la estadía?",
    "¿el spa está abierto todo el día?",
    "quiero saber si el servicio de spa tiene costo adicional",
    "¿tienen masajes profesionales en el hotel?",
    "¿el centro de bienestar cuenta con tratamientos?",
    "¿puedo pedir masajes y relajación?",
    "quiero saber si puedo usar el spa del hotel",
    "¿el hotel ofrece tratamientos de bienestar?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "durante la estadía", "en el centro de bienestar"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el spa", "los masajes", "el centro de bienestar", "tratamientos de relajación"]

# Errores comunes
errores_comunes = {
    "spa": ["spa", "spá", "spa"],
    "masajes": ["masajes", "masajess", "masajes"],
    "bienestar": ["bienestar", "bienestar", "bienenstar"],
    "tratamientos": ["tratamientos", "tratamietos", "tratamientos"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_spa_masajes"
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
