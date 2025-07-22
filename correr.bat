@echo off
title Eugenia

:: Cambiar a la carpeta del script
cd /d "%~dp0"

:: Verificar si python está disponible
where python >nul 2>nul
if errorlevel 1 (
    echo Python no está instalado o no está en el PATH.
    pause
    exit /b
)

:: Verificar si uvicorn está instalado
python -c "import uvicorn" 2>nul
if errorlevel 1 (
    echo Uvicorn no está instalado. Ejecuta: pip install fastapi uvicorn
    pause
    exit /b
)

:: Iniciar el servidor
echo Iniciando servidor FastAPI...
python app.py

pause
