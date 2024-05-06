#!/usr/bin/env python3
# AULAUNIVERSAL 2024
import os
import platform
import psutil
import netifaces
import os
import time

# Dibujo con letras "AULAUNIVERSAL" usando diferentes caracteres
logo = """
  ___    ____   __   __  _       ____    _____   ____    _____    ____    _   _   _
              aaaaaaaaaaaaaaaaaa    aaaa      aaaa  aaaa          aaaaaaaaaaaaaaaaa
              aaaa         aaaaa    aaaa      aaaa  aaaa          aaaa         aaaa
              aaaa         aaaaa    aaaa      aaaa  aaaa          aaaa         aaaa  
              aaaaaaaaaaaaaaaaaa    aaaa      aaaa  aaaa          aaaaaaaaaaaaaaaaa  
              aaaa         aaaaa    aaaa      aaaa  aaaaaaaaaaaa  aaaa         aaaa
              aaaa         aaaaa    aaaaaaaaaaaaaa  aaaaaaaaaaaa  aaaa         aaaa 
                   
                          
              uu  uu  uu   uu  uu  uu    uu uuuuuu  uuuuu    uuuuuu  uuuuuu  uu 
              uu  uu  uu u uu  uu   uu  uu  uuu     uu u u      uu   uuuuuu  uu
              uuuuuu  uu   uu  uu     u     uuuuuu  uu    u   uuuuuu uu  uu  uuuuuu
                                 Version 1.0  Aulauniversal 2024 ,Windows, Linux, Android
                
"""

# Mostrar el logo en pantalla
print(logo)

# Pausa de 2 segundos
time.sleep(4)

# Continuar con el resto del script aquí
# ...



# Obtener la ruta del directorio actual donde se ejecuta el script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Definir los nombres de los directorios para cada versión del software en Android
android_directories = {
    "9.03": "_internal/PS4_stage_bin_all/PS4-9.03/",
    "9.04": "_internal/PS4_stage_bin_all/PS4-9.04/",
    "9.50": "_internal/PS4_stage_bin_all/PS4-9.50/",
    "9.51": "_internal/PS4_stage_bin_all/PS4-9.51/",
    "9.60": "_internal/PS4_stage_bin_all/PS4-9.60/",
    "10.00": "_internal/PS4_stage_bin_all/PS4-9.61/",
    "10.01": "_internal/PS4_stage_bin_all/PS4-10.01/",
    "10.50": "_internal/PS4_stage_bin_all/PS4-10.50/",
    "10.70": "_internal/PS4_stage_bin_all/PS4-10.70/",
    "10.71": "_internal/PS4_stage_bin_all/PS4-10.71/",
    "11.00": "_internal/PS4_stage_bin_all/PS4-11.00/"
}

# Definir los nombres de los directorios para cada versión del software en otros sistemas
other_system_directories = {
    "9.00": os.path.join(current_directory, "PS4_stage_bin_all/PS4-9.00/"),
    "9.03": os.path.join(current_directory, "PS4_stage_bin_all/PS4-9.03/"),
    "9.04": os.path.join(current_directory, "PS4_stage_bin_all/PS4-9.04/"),
    "9.50": os.path.join(current_directory, "PS4_stage_bin_all/PS4-9.50/"),
    "9.51": os.path.join(current_directory, "PS4_stage_bin_all/PS4-9.51/"),
    "9.60": os.path.join(current_directory, "PS4_stage_bin_all/PS4-9.60/"),
    "10.00": os.path.join(current_directory, "PS4_stage_bin_all/PS4-9.61/"),
    "10.01": os.path.join(current_directory, "PS4_stage_bin_all/PS4-10.01/"),
    "10.50": os.path.join(current_directory, "PS4_stage_bin_all/PS4-10.50/"),
    "10.70": os.path.join(current_directory, "PS4_stage_bin_all/PS4-10.70/"),
    "10.71": os.path.join(current_directory, "PS4_stage_bin_all/PS4-10.71/"),
    "11.00": os.path.join(current_directory, "PS4_stage_bin_all/PS4-11.00/")
}

# Función para obtener las interfaces de red según el sistema operativo
def obtener_interfaces(sistema_operativo):
    if sistema_operativo == "Windows":
        # Obtener interfaces de red en Windows
        interfaces = [interface for interface, addrs in psutil.net_if_addrs().items() if addrs]
    elif sistema_operativo == "Linux":
        # Obtener interfaces de red en Linux
        interfaces = [interface for interface in netifaces.interfaces() if interface.startswith(("eth", "enp"))]
    elif sistema_operativo == "Android":
        # Obtener interfaces de red en Android (Termux)
        interfaces_str = os.popen("ifconfig").read()
        interfaces = [line.split()[0] for line in interfaces_str.split('\n') if 'mtu' in line]
    else:
        print(f"El sistema operativo {sistema_operativo} no está soportado.")
        exit(1)
    
    return interfaces


# Mostrar la lista de versiones disponibles
print("Selecciona una versión para lanzar en la PS4:")
if platform.system() == "Android":
    # Mostrar solo las versiones disponibles para Android
    for index, version in enumerate(android_directories.keys(), 1):
        print(f"{index}. {version}")
    directories = android_directories
else:
    # Mostrar todas las versiones disponibles
    for index, version in enumerate(other_system_directories.keys(), 1):
        print(f"{index}. {version}")
    directories = other_system_directories

# Leer la opción seleccionada por el usuario
opcion = int(input("Ingresa el número correspondiente a la versión que deseas lanzar: "))
if opcion < 1 or opcion > len(directories):
    print("Opción inválida. Por favor, selecciona un número válido.")
    exit(1)

# Obtener el directorio correspondiente a la versión seleccionada
version_seleccionada = list(directories.keys())[opcion - 1]
directorio_seleccionado = directories[version_seleccionada]

# Seleccionar el sistema operativo
print("Selecciona el sistema operativo:")
print("1. Windows")
print("2. Linux")
print("3. Android")
sistema_operativo_index = int(input("Ingresa el número correspondiente al sistema operativo que estás utilizando: "))
if sistema_operativo_index == 1:
    sistema_operativo = "Windows"
elif sistema_operativo_index == 2:
    sistema_operativo = "Linux"
elif sistema_operativo_index == 3:
    sistema_operativo = "Android"
else:
    print("Opción inválida. Por favor, selecciona un número válido.")
    exit(1)

# Obtener las interfaces de red disponibles
interfaces = obtener_interfaces(sistema_operativo)
if not interfaces:
    print("No se encontraron interfaces de red disponibles.")
    exit(1)

# Seleccionar el interfaz de red
print("Selecciona el interfaz de red:")
for index, interface in enumerate(interfaces, 1):
    print(f"{index}. {interface}")
interfaz_index = int(input("Ingresa el número correspondiente al interfaz de red que deseas usar: "))
selected_interface = interfaces[interfaz_index - 1]

# Generar y ejecutar el comando final
if sistema_operativo == "Windows":
    comando = f"python pppwn.py --interface=\"{selected_interface}\" --fw={version_seleccionada.replace('.', '')}"
elif sistema_operativo == "Linux":
    comando = f"python3 pppwn.py --interface={selected_interface} --fw={version_seleccionada.replace('.', '')}"
elif sistema_operativo == "Android":
    comando = f"python pppwn.py --interface={selected_interface} --fw={version_seleccionada.replace('.', '')}"
else:
    print("Sistema operativo no compatible.")
    exit(1)

os.chdir(directorio_seleccionado)  # Cambiar al directorio seleccionado
os.system(comando)

