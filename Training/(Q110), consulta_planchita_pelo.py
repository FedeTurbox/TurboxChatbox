# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre planchita de pelo
frases_base = [
    "¿hay planchita de pelo?",
    "quiero saber si tienen planchita de pelo",
    "¿el hotel ofrece planchita para el cabello?",
    "¿tienen plancha para el pelo disponible?",
    "quiero consultar por la planchita de pelo",
    "¿hay planchita en la habitación?",
    "¿puedo usar planchita de pelo?",
    "¿ofrecen plancha para cabello?",
    "¿la planchita de pelo está incluida?",
    "quiero saber si hay planchita para el cabello",
    "¿hay plancha para los huéspedes?",
    "¿el hotel cuenta con planchita de pelo?",
    "¿tienen planchita para uso personal?",
    "quiero saber si puedo usar planchita",
    "¿hay planchita de pelo disponible?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "la planchita de pelo", "la plancha", "planchita para el cabello"]

# Errores comunes
errores_comunes = {
    "planchita": ["planchita", "planchíta", "planchita"],
    "pelo": ["pelo", "pello", "pelo"],
    "cabello": ["cabello", "cabeyo", "cabello"],
    "hotel": ["hotel", "hotel", "hottel"],
    "habitación": ["habitacion", "habitación", "habítacion"]
}

nombre_base = "consulta_planchita_pelo"
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
