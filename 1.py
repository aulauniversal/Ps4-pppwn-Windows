#!/usr/bin/env python3
# AULAUNIVERSAL 2024
import os
import platform
import psutil
import netifaces

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

# Definir los nombres de los directorios para cada versión del software en Windows y Linux
other_system_directories = {
    "9.00": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-9.00/"),
    "9.03": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-9.03/"),
    "9.04": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-9.04/"),
    "9.50": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-9.50/"),
    "9.51": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-9.51/"),
    "9.60": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-9.60/"),
    "10.00": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-9.61/"),
    "10.01": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-10.01/"),
    "10.50": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-10.50/"),
    "10.70": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-10.70/"),
    "10.71": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-10.71/"),
    "11.00": os.path.join(current_directory, "_internal/PS4_stage_bin_all/PS4-11.00/")
}

# Función para obtener las interfaces de red según el sistema operativo
def obtener_interfaces(sistema_operativo):
    if sistema_operativo == "Windows":
        # Obtener interfaces de red en Windows
        interfaces = [interface for interface, addrs in psutil.net_if_addrs().items() if addrs]
    elif sistema_operativo == "Linux":
        # Obtener interfaces de red en Linux
        interfaces = netifaces.interfaces()
    elif sistema_operativo == "Android":
        # Obtener interfaces de red en Android (Termux)
        interfaces_str = os.popen("ip link").read()
        interfaces = [line.split()[1][:-1] for line in interfaces_str.split('\n') if line.strip() and 'lo:' not in line]
    else:
        print(f"El sistema operativo {sistema_operativo} no está soportado.")
        exit(1)
    
    # Filtrar solo las interfaces cableadas
    if sistema_operativo != "Windows":
        interfaces = [interface for interface in interfaces if interface.lower().startswith(("eth", "enp"))]
    
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
comando = f"python pppwn.py --interface=\"{selected_interface}\" --fw={version_seleccionada.replace('.', '')}"
os.chdir(directorio_seleccionado)  # Cambiar al directorio seleccionado
os.system(comando)
