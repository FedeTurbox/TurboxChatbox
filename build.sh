#!/usr/bin/env bash

Script para configurar el entorno en Render.
Salir inmediatamente si un comando falla.
set -e

echo "--- Instalando dependencias de Python ---"
pip install -r requirements.txt

echo "--- Descargando datos de NLTK ---"
python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4'); nltk.download('punkt'); nltk.download('punkt_tab');"

echo "--- Construcción finalizada exitosamente ---"