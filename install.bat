@echo off
rem Este script instalará las dependencias del archivo requirements.txt

pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Hubo un error durante la instalación de los paquetes.
    pause
    exit /b %errorlevel%
)

echo Instalación completada correctamente.
pause
