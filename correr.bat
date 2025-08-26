@echo off
title Eugenia - Iniciando...

:: Cambiar a la carpeta del script
cd /d "%~dp0"

echo Verificando dependencias...

:: Verificar si python esta disponible
where python >nul 2>nul
if errorlevel 1 (
    echo.
    echo -----------------------------------------------------------------
    echo  ERROR: Python no esta instalado o no esta en el PATH.
    echo  Por favor, instala Python desde python.org y asegurate
    echo  de marcar la casilla "Add Python to PATH" durante la instalacion.
    echo -----------------------------------------------------------------
    echo.
    pause
    exit /b
)

:: --- Verificacion e instalacion de dependencias ---
python -c "import fastapi, uvicorn, sentence_transformers, torch, nltk, multipart" >nul 2>nul
if errorlevel 1 (
    echo.
    echo Dependencias faltantes. Intentando instalar...
    echo (Esto puede tardar varios minutos la primera vez)
    echo.
    pip install fastapi uvicorn sentence-transformers torch nltk python-multipart
    if errorlevel 1 (
        echo.
        echo -----------------------------------------------------------------
        echo  ERROR: Fallo la instalacion de dependencias.
        echo  Intenta ejecutar este comando manualmente en una terminal:
        echo  pip install fastapi uvicorn sentence-transformers torch nltk python-multipart
        echo -----------------------------------------------------------------
        echo.
        pause
        exit /b
    )
    echo.
    echo Dependencias instaladas correctamente.
    echo.
) else (
    echo Dependencias ya instaladas.
)

echo.
echo Descargando datos de NLTK...
python -c "import nltk; nltk.download('wordnet', quiet=True); nltk.download('omw-1.4', quiet=True); nltk.download('punkt', quiet=True); nltk.download('punkt_tab', quiet=True)"

:: Iniciar el servidor y abrir el navegador
echo.
echo Iniciando servidor FastAPI...
echo.

:: Abre el navegador apuntando a la primera instancia por defecto
start "" "http://127.0.0.1:5000/1"

:: Inicia el servidor Uvicorn. Este comando tomara el control de la ventana.
python -m uvicorn app:app --host 127.0.0.1 --port 5000

pause
