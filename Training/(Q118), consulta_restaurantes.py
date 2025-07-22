# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre restaurantes
frases_base = [
    "¿pueden recomendar restaurantes cerca?",
    "quiero saber si hay restaurantes en la zona",
    "¿el hotel tiene restaurante propio?",
    "¿tienen recomendaciones de lugares para comer?",
    "quiero consultar por restaurantes cerca del hotel",
    "¿hay buenos restaurantes en los alrededores?",
    "¿puedo pedir sugerencias de restaurantes?",
    "¿ofrecen servicio de restaurante en el hotel?",
    "¿el restaurante del hotel está abierto al público?",
    "quiero saber si hay opciones para cenar cerca",
    "¿tienen lista de restaurantes recomendados?",
    "¿el hotel cuenta con restaurante?",
    "¿hay restaurantes abiertos las 24 horas cerca?",
    "quiero saber si puedo cenar en el hotel",
    "¿ofrecen información sobre restaurantes locales?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "cerca del hotel", "en la zona", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "restaurantes recomendados", "el restaurante del hotel", "lugares para comer"]

# Errores comunes
errores_comunes = {
    "restaurante": ["restaurante", "restorante", "restaurrante"],
    "restaurantes": ["restaurantes", "restorantes", "restaurantes"],
    "hotel": ["hotel", "hottel", "hotel"],
    "comer": ["comer", "comér", "comer"],
    "cena": ["cena", "sena", "cena"]
}

nombre_base = "consulta_restaurantes"
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
