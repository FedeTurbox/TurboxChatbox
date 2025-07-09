@echo off
title Chat Hotel Libertadores - Servidor

:: Cambiar a la carpeta del script
cd /d "%~dp0"

:: Verificar si python está disponible
where python >nul 2>nul
if errorlevel 1 (
    echo Python no está instalado o no está en el PATH.
    pause
    exit /b
)

:: Ejecutar app.py
echo Iniciando servidor Flask...
start "" http://127.0.0.1:5000
python app.py

pause
