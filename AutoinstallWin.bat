@echo off
REM AULAUNIVERSAL 2024
REM Instalacion de Python
echo Instalando Python...
start /w "" https://www.python.org/downloads/
echo BIENVENIDO AL INSTALADOR AUTOMATICO AULAUNIVERSAL 2024 PS4 PPPWN THEFLOW******
echo Deberas de instalar python manualmente y hasta que no lo tengas instalado
echo NO PROSIGAS CON LA INSTALACION
echo repite la accion si te da error al instalar todo lo demas sin python
echo Asegurate de seleccionar la opcion "Agregar Python 3.x al PATH" durante la instalacion.

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
