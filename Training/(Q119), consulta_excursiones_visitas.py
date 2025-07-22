# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre excursiones y visitas guiadas
frases_base = [
    "¿ofrecen excursiones desde el hotel?",
    "quiero saber si hay visitas guiadas disponibles",
    "¿el hotel organiza excursiones?",
    "¿tienen servicio de tours o visitas guiadas?",
    "quiero consultar por excursiones en la zona",
    "¿hay visitas guiadas para huéspedes?",
    "¿puedo contratar excursiones en el hotel?",
    "¿ofrecen excursiones a lugares turísticos?",
    "¿el servicio de excursiones tiene costo adicional?",
    "quiero saber si hay tours organizados",
    "¿tienen visitas guiadas a atracciones locales?",
    "¿el hotel cuenta con excursiones propias?",
    "¿hay excursiones para recorrer la ciudad?",
    "quiero saber si puedo solicitar visitas guiadas",
    "¿ofrecen tours guiados para los huéspedes?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "durante la estadía", "cerca del hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "las excursiones", "las visitas guiadas", "los tours turísticos"]

# Errores comunes
errores_comunes = {
    "excursiones": ["excursiones", "excurciones", "excursiones"],
    "visitas": ["visitas", "visittas", "visitas"],
    "guiadas": ["guiadas", "guiadass", "guyadas"],
    "tours": ["tours", "turss", "tours"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_excursiones_visitas"
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
