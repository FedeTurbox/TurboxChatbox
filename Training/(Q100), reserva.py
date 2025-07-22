# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para reservas genéricas
frases_base = [
    "quiero realizar una reserva",
    "me gustaría hacer una reserva",
    "deseo reservar",
    "quiero reservar",
    "quiero hacer una reserva",
    "necesito reservar",
    "me gustaría reservar",
    "quiero agendar una reserva",
    "quiero apartar un lugar",
    "quiero reservar un turno",
    "quiero solicitar una reserva",
    "quiero confirmar una reserva",
    "quiero hacer una cita",
    "me gustaría hacer una cita",
    "quiero agendar una cita",
    "quiero pedir una reserva",
    "quiero gestionar una reserva"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "para hoy", "para mañana", "para la fecha indicada"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "una reserva", "un turno", "una cita"]

# Errores comunes
errores_comunes = {
    "reserva": ["reseva", "rezerba", "resrva"],
    "quiero": ["kiero", "quero", "quierro"],
    "hacer": ["aser", "acer", "hazer"],
    "una": ["una", "una", "una"],
    "cita": ["sita", "sita", "citta"],
    "turno": ["turnoo", "turmo", "turmo"]
}

nombre_base = "reserva_usuario"
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
