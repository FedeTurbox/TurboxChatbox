# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre pack fútbol y decodificador
frases_base = [
    "¿tienen pack de fútbol en la TV?",
    "quiero saber si ofrecen canales de fútbol local",
    "¿el hotel ofrece decodificador para ver fútbol?",
    "¿hay canales premium de fútbol disponibles?",
    "quiero consultar por el pack de fútbol",
    "¿puedo ver fútbol local en la habitación?",
    "¿ofrecen fútbol premium en la televisión?",
    "¿tienen canales para partidos de fútbol?",
    "¿el hotel cuenta con decodificador para deportes?",
    "quiero saber si hay pack de fútbol para huéspedes",
    "¿ofrecen fútbol local y premium?",
    "¿puedo usar el decodificador para ver fútbol?",
    "quiero consultar si hay canales de fútbol premium",
    "¿el hotel tiene fútbol local en la TV?",
    "¿hay pack fútbol disponible en las habitaciones?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "durante la estadía", "en el hotel"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "pack de fútbol", "canales de fútbol", "decodificador", "fútbol local", "fútbol premium"]

# Errores comunes
errores_comunes = {
    "fútbol": ["futbol", "fútbol", "futbol"],
    "decodificador": ["decodificador", "decodficador", "decodificador"],
    "premium": ["premium", "preminum", "premiun"],
    "hotel": ["hotel", "hottel", "hotel"],
    "canales": ["canales", "canalls", "canales"]
}

nombre_base = "consulta_pack_futbol"
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
