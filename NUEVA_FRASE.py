# -*- coding: utf-8 -*-

from Generador import generar_con_errores

# Ejemplo de uso con una frase base estática
frase_base_ejemplo = "quiénes están en la reunión"
nombre_base = "consulta_quienes_reunion"

# Definición de errores comunes para la frase
errores_comunes_ejemplo = {
    "reunión": ["reunion", "reunon", "renion"],
    "quiénes": ["quienes", "kienés", "kien"],
    "participantes": ["participantes", "partisipantes"],
    "presentes": ["presentes", "presentez", "presntes"],
    "asistentes": ["asistentez", "acistentes"]
}

# Generar frases
generar_con_errores(
    frase_base=frase_base_ejemplo,
    errores_comunes=errores_comunes_ejemplo,
    nombre_base=nombre_base,
    n_perfectas=200
)
