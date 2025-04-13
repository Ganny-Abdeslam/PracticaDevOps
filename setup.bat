@echo off
REM Crear entorno virtual
python -m venv venv

REM Activar entorno virtual
call venv\Scripts\activate

REM Instalar dependencias
pip install -r requirements.txt

echo -----------------------------------
echo Entorno creado y dependencias listas.
echo Usa "venv\Scripts\activate" para activar manualmente tu entorno en otra terminal.
