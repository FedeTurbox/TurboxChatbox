# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre pet friendly / mascotas
frases_base = [
    "¿el hotel es pet friendly?",
    "quiero saber si aceptan mascotas",
    "¿puedo llevar a mi perro?",
    "¿aceptan gatos en las habitaciones?",
    "quiero consultar si se permiten mascotas",
    "¿el hotel admite animales domésticos?",
    "¿hay restricciones para llevar mascotas?",
    "¿aceptan aves o pájaros como mascotas?",
    "¿puedo hospedarme con mi gato?",
    "quiero saber si permiten perros pequeños",
    "¿se aceptan loros u otras aves?",
    "¿el hotel permite mascotas en las habitaciones?",
    "¿puedo reservar llevando mi mascota?",
    "¿aceptan mascotas durante la estadía?",
    "quiero saber si hay cargos extra por mascotas"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "las mascotas", "perros y gatos", "animales domésticos", "aves o pájaros"]

# Errores comunes
errores_comunes = {
    "mascotas": ["mascotas", "mascotass", "mascotas"],
    "pet friendly": ["pet friendly", "petfrendly", "pet frendly"],
    "perros": ["perros", "perrros", "peros"],
    "gatos": ["gatos", "gattos", "gatos"],
    "aves": ["aves", "aves", "avez"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_pet_friendly"
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
