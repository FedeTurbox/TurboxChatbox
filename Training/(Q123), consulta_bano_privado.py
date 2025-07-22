# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre baño privado
frases_base = [
    "¿las habitaciones tienen baño privado?",
    "quiero saber si hay baño privado en la habitación",
    "¿el hotel ofrece habitaciones con baño privado?",
    "¿tienen baño privado para los huéspedes?",
    "quiero consultar por baño privado en las habitaciones",
    "¿hay baño privado disponible?",
    "¿puedo reservar habitación con baño privado?",
    "¿ofrecen habitaciones con baño propio?",
    "¿el baño privado está incluido en la habitación?",
    "quiero saber si el baño es privado o compartido",
    "¿las habitaciones cuentan con baño exclusivo?",
    "¿hay baño privado en todas las habitaciones?",
    "¿el hotel tiene habitaciones con baño privado?",
    "quiero consultar si el baño es privado",
    "¿ofrecen baño privado para los huéspedes?"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en la habitación", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el baño privado", "baño propio", "baño exclusivo"]

# Errores comunes
errores_comunes = {
    "baño": ["baño", "bano", "baño"],
    "privado": ["privado", "pribado", "privado"],
    "habitación": ["habitacion", "habitación", "habítacion"],
    "hotel": ["hotel", "hottel", "hotel"]
}

nombre_base = "consulta_bano_privado"
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
