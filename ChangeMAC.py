import os
import subprocess
import re

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
	mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)

if mac_address_search_result:
	return mac_address_search_result.group(0)
else:
	print("No se pudo obtener la dirección MAC actual.")

def change_mac(interface, new_mac):
	print(f"Cambiando la dirección MAC de {interface} a {new_mac}")
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

# Ingresa la interfaz y la nueva dirección MAC
interface = "eth0" # Puedes ajustar la interfaz según tu sistema
new_mac = "00:11:22:33:44:55" # Ajusta la nueva dirección MAC que deseas

# Mostrar la dirección MAC actual
current_mac = get_current_mac(interface)
print(f"MAC actual de {interface}: {current_mac}")

# Cambiar la dirección MAC
change_mac(interface, new_mac)

# Verificar si la dirección MAC ha sido cambiada correctamente
current_mac = get_current_mac(interface)
print(f"MAC después del cambio: {current_mac