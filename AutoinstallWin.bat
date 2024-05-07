@echo off
REM AULAUNIVERSAL 2024
REM Instalación de Python
echo Instalando Python...
start /w "" https://www.python.org/downloads/
echo Debrás de instalar python manualmente y hasta que no lo tengas instalado
echo NO PROSIGAS CON LA INSTALACIÓN
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
