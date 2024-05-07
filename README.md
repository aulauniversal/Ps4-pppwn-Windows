Imprescindible tener instalado todo este software en orden para evitar fallos de instalación,
descargar Python desde página oficial
https://www.python.org/downloads/

*Instalar Python-En proceso de instalación clickear ambas casillas seleccionable PIP

*Instalar Ncap (Archivo incluido)

*Instalar Scapy ---Comando desde consola CMD : pip install scapy

*Requerimientos Python :    pip install -r requirements.txt

***ACTUALIZACIÓN***
-Añadido archivo auto instalable .BAT 
-Modificación de archivo start.py LINUX OK , WINDOWS OK , Android Emulator OK , Real ???? sin poder probar 

***ACTUALIZACIÓN***
-ACTUALIZADO STAGE2.BIN 11.00 LOADER STABLE
-ACTUALIZADO RECOPILACION PAYLOADS 11.00
-ARCHIVO START.PY VALIDO PARA ANDROID (TELEFONO ROOTEADO Y TERMUX Y TODAS LAS DEPENDENCIAS REQUERIDAS)


***ACTUALIZACIÓN***
Sustituir la carga util "stage2.bin" por el requerido por el usuario , ya se encuentra disponible  tanto
LoaderUSB como modo DebugSystem para version 11.00
La ubicación a sustituir es     /_internal/PS4_stage_bin_all/XxXVersion/stage2/

Eliminar el archivo existente stage2.bin y sustituir por el seleccionado, renombrar este como el archivo de origen "stage2.bin"

Ejecutar Start.exe 

Valido para todas las versiones dese 9.00 hasta 11.00 
Payload inyectable solo con versión 9.00 y 11.00 de momento, incluye payload y GoldHen(la instalacion es sencilla , copiar el GoldHen.bin y copiar en raiza de USb
formateado en fat32 , renombrarlo a payload.bin, ejecutar Start.exe y seguir las instarucciones.
Todo esto no sería posible sin la ayuda de nuestro amigo
TheFlow y la vulneravilidad encontrada https://hackerone.com/reports/2177925 ( CVE-2006-4304)

https://github.com/TheOfficialFloW/PPPwn
