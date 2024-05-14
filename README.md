AVISO IMPORTANTE CON LA NUEVA ACTUALIZACION PPPWN C++ , EL PROCESO DE CARGA NO ES VISUAL, ES EN SEGUNDO PLANO ,CUANDO TERMINA LA EJECUCION SE CIERRA EL PROGRAMA , REINTENTAR SI A LA PRIMERA NO FUNCIONA , PERO SOLO COMENTAR QUE CON ESTA NUEVA VERSION DE CARGA NO SE PRINTEA EN PANTALLA EL PROCESO DE CARGA...UN SALUDO A TODOS

En Linux es sencillo solo instalar los requerimientos :

python y pip instalado


pip install -r requirements.txt

y ejecutar start.py :

python3 start.py o python start.py


Instrucciones mas detalladas en el video para hacerlo funcionar en todos los sistemas posibles excepto MAC

https://www.youtube.com/watch?v=xk5VTApAl-M

Imprescindible tener instalado todo este software en orden para evitar fallos de instalación,
descargar Python desde página oficial
https://www.python.org/downloads/

*WINDOWS

Ejecutar Autoinstall.bat

instalar python lo primero , sin eso lo demás del proceso dará fallo lo demás se instalará todo automáticamente menos ncap que tendréis que aceptar la instalación sin más , si a la primera falla volver a probar , sin python no va a funcionar , cuando tengáis python reintentad e irá bien .

ejecutar start.wxe cuando esté todo OK


***ACTUALIZACIÓN***

Incluido Loader nuevo stage1 + stage2 + pppwn C++ Stable Solo para versiones 11.00 activo. Windows y Linux


***ACTUALIZACIÓN***

GOLDHEN ACTUALIZADO PARA VERSION 11.00, EL CARGADOR YA SE ENCUENTRA EN STAGE2 SOLO HAY QUE METER EL PAYLOAD AL USB Y EJECUTAR

*******************


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
