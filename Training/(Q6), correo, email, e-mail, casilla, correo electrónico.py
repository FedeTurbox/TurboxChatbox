# -*- coding: utf-8 -*-

from Generador import generar_con_errores, pedir_qx

# Frases base
frases_base = [
    "cual es el correo electronico",
    "puede darme el mail",
    "me puede dar el email",
    "podria decirme la casilla de correo",
    "me podria dar la direccion de email",
    "necesito el correo electronico",
    "puede indicarme la casilla de correo",
    "quiero saber la direccion de email",
    "podria darme el correo",
    "cual es el mail de contacto",
    "me da el correo electronico",
    "me puede facilitar el email",
    "seria tan amable de darme la casilla de correo",
    "necesito saber el correo",
    "puede decirme la direccion de correo"
]

# Componentes dinamicos
verbos = ["", "podria", "puede", "me podria", "quisiera"]
adverbios = ["", "por favor", "ahora", "cuando pueda"]
acciones = ["darme", "facilitarme", "indicarme", "decirme", "proporcionarme"]
objetos = [
    "el correo",
    "el correo electronico",
    "el mail",
    "el email",
    "la casilla de correo",
    "la direccion de email",
    "la direccion de correo",
    "el correo de contacto",
    "el mail de contacto"
]

# Errores comunes
errores_comunes = {
    "correo": ["coreo", "correoo", "correo"],
    "electronico": ["electrónico", "eletronico", "electróniko", "electronico"],
    "mail": ["mail", "mail", "maill", "mayl"],
    "email": ["emal", "imeil", "e-mail", "email"],
    "casilla": ["casila", "cazilla", "casilla"],
    "direccion": ["direcion", "dirreccion", "direxion", "dirección"],
    "contacto": ["contactto", "kontacto", "contacot"]
}

nombre_base = "pregunta_correo"
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
