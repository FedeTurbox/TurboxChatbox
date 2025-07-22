# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre televisión y smart TV
frases_base = [
    "¿la habitación tiene televisión?",
    "quiero saber si hay smart TV disponible",
    "¿ofrecen televisión en las habitaciones?",
    "¿las habitaciones cuentan con smart TV?",
    "quiero consultar por la televisión",
    "¿hay televisión para los huéspedes?",
    "¿puedo usar la smart TV durante mi estadía?",
    "¿la televisión está incluida en la habitación?",
    "quiero saber si la smart TV tiene acceso a internet",
    "¿el hotel ofrece smart TV en las habitaciones?",
    "¿hay canales por cable o satélite?",
    "¿la habitación tiene pantalla inteligente?",
    "¿puedo conectar dispositivos a la smart TV?",
    "quiero consultar si la televisión es smart TV",
    "¿ofrecen televisión con servicios inteligentes?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "durante la estadía", "en el hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "la televisión", "smart TV", "televisión inteligente", "pantalla inteligente"]

# Errores comunes
errores_comunes = {
    "televisión": ["television", "televisión", "televison"],
    "smart TV": ["smart tv", "smar tv", "smartt tv"],
    "hotel": ["hotel", "hottel", "hotel"],
    "pantalla": ["pantalla", "pantaya", "pantalla"]
}

nombre_base = "consulta_television_smarttv"
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
