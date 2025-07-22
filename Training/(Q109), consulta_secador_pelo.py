# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre secador de pelo
frases_base = [
    "¿hay secador de pelo?",
    "quiero saber si tienen secador de pelo",
    "¿el hotel ofrece secador de cabello?",
    "¿tienen secador disponible?",
    "quiero consultar por el secador de pelo",
    "¿hay secador en la habitación?",
    "¿puedo usar secador de pelo?",
    "¿ofrecen secador de cabello?",
    "¿el secador de pelo está incluido?",
    "quiero saber si hay secador de cabello",
    "¿hay secador para los huéspedes?",
    "¿el hotel cuenta con secador de pelo?",
    "¿tienen secador para uso personal?",
    "quiero saber si puedo usar secador",
    "¿hay secador de pelo disponible?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el secador de pelo", "el secador", "secador de cabello"]

# Errores comunes
errores_comunes = {
    "secador": ["secador", "secadr", "secador"],
    "pelo": ["pelo", "pello", "pelo"],
    "cabello": ["cabello", "cabeyo", "cabello"],
    "hotel": ["hotel", "hotel", "hottel"],
    "habitación": ["habitacion", "habitación", "habítacion"]
}

nombre_base = "consulta_secador_pelo"
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
