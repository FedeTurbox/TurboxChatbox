# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre recomendaciones de paseos / atracciones
frases_base = [
    "¿pueden recomendar paseos turísticos?",
    "quiero saber si ofrecen información sobre atracciones",
    "¿el hotel tiene recomendaciones de excursiones?",
    "¿tienen servicio de asesoramiento turístico?",
    "quiero consultar por paseos recomendados en la zona",
    "¿hay información sobre lugares para visitar?",
    "¿puedo pedir recomendaciones de atracciones?",
    "¿ofrecen excursiones o paseos guiados?",
    "¿el hotel brinda información turística?",
    "quiero saber si hay atracciones cerca del hotel",
    "¿tienen mapas o guías de turismo?",
    "¿el hotel cuenta con servicio de información turística?",
    "¿hay paseos organizados para los huéspedes?",
    "quiero saber si puedo pedir recomendaciones de turismo",
    "¿ofrecen asesoramiento para excursiones?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la ciudad", "cerca del hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "paseos turísticos", "atracciones turísticas", "excursiones", "información turística"]

# Errores comunes
errores_comunes = {
    "paseos": ["paseos", "paceos", "paseoss"],
    "atracciones": ["atracciones", "atraciónes", "atracciones"],
    "turísticas": ["turisticas", "turísticas", "turístikas"],
    "excursiones": ["excursiones", "excurciones", "excursiones"],
    "turismo": ["turismo", "turizmo", "turísmo"]
}

nombre_base = "consulta_paseos_atracciones"
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
