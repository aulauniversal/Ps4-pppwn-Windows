@echo off
REM AULAUNIVERSAL 2024
REM Instalación de Python
echo Instalando Python...
start /w "" python-3.10.0-amd64.exe
echo Asegúrate de seleccionar la opción "Agregar Python 3.x al PATH" durante la instalación.

REM Instalación de Npcap
echo Instalando Npcap...
start /w "" npcap-1-79.exe
REM Sigue las instrucciones de instalación de Npcap.

REM Instalación de Scapy
echo Instalando Scapy...
pip install scapy

REM Instalación de otras dependencias de Python
echo Instalando otras dependencias de Python...
pip install -r requirements.txt

echo Instalación completada.
pause
