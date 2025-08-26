@echo off
title Generador de Consultas para Instancias

:: Pedir el ID de la instancia
set /p instance_id="> Introduce el ID de la instancia (ej. 1): "
if not defined instance_id (
    echo.
    echo ERROR: No se introdujo un ID de instancia.
    pause
    exit /b
)

:: Pedir la frase base
set /p frase="> Introduce la frase base para generar consultas: "
if not defined frase (
    echo.
    echo ERROR: No se introdujo una frase.
    pause
    exit /b
)

echo.
echo Procesando para instancia '%instance_id%' la frase: "%frase%"
echo --------------------------------------------------
python Generador.py "%instance_id%" "%frase%"
echo --------------------------------------------------
echo.
pause
