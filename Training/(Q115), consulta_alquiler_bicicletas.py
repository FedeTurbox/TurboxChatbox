# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre alquiler de bicicletas
frases_base = [
    "¿hay alquiler de bicicletas?",
    "quiero saber si alquilan bicicletas",
    "¿el hotel ofrece bicicletas para alquilar?",
    "¿tienen servicio de alquiler de bicis?",
    "quiero consultar por el alquiler de bicicletas",
    "¿puedo alquilar una bicicleta en el hotel?",
    "¿hay bicicletas disponibles para huéspedes?",
    "¿ofrecen bicicletas en alquiler?",
    "¿el alquiler de bicicletas tiene costo adicional?",
    "quiero saber si hay bicis para alquilar",
    "¿tienen bicicletas para uso de los huéspedes?",
    "¿el hotel cuenta con servicio de bicicletas?",
    "¿hay bicicletas para recorrer la zona?",
    "quiero saber si puedo usar una bicicleta del hotel",
    "¿el alquiler de bicis está incluido en la estadía?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en el hotel", "durante la estadía", "para recorrer la ciudad"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el alquiler de bicicletas", "bicicletas en alquiler", "el servicio de bicis"]

# Errores comunes
errores_comunes = {
    "bicicletas": ["bicicletas", "bicicletass", "visicletas"],
    "bici": ["bici", "vici", "bicy"],
    "alquiler": ["alquiler", "alqiler", "alquyler"],
    "hotel": ["hotel", "hottel", "hotel"],
    "servicio": ["servicio", "servisio", "servicio"]
}

nombre_base = "consulta_alquiler_bicicletas"
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
