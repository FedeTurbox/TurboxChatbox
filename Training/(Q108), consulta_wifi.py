# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base para preguntas sobre wifi
frases_base = [
    "¿tienen wifi disponible?",
    "quiero saber si hay wifi",
    "¿el hotel ofrece wifi gratis?",
    "¿hay conexión wifi en las habitaciones?",
    "quiero consultar por el wifi",
    "¿el wifi tiene costo?",
    "¿hay internet inalámbrico?",
    "quiero saber si el wifi es gratuito",
    "¿tienen señal wifi en todo el hotel?",
    "¿ofrecen wifi durante la estadía?",
    "¿el wifi está incluido?",
    "quiero saber si puedo conectarme a wifi",
    "¿el wifi funciona bien?",
    "¿hay acceso a internet wifi?",
    "quiero consultar si el wifi es gratis"
]

# Componentes dinámicos
verbos = ["", "por favor", "ahora", "lo antes posible"]
adverbios = ["", "en las habitaciones", "en el hotel", "durante la estadía"]
acciones = ["", "con anticipación", "de inmediato"]
objetos = ["", "el wifi", "la conexión wifi", "el internet inalámbrico"]

# Errores comunes
errores_comunes = {
    "wifi": ["wifi", "wify", "wifii"],
    "internet": ["internet", "intenet", "internét"],
    "conexión": ["conexion", "conexión", "conexon"],
    "disponible": ["disponible", "disponble", "disponiblle"]
}

nombre_base = "consulta_wifi"
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
