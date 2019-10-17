# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2019-10-03T07:13:54-04:00
# @Last modified by:   root
# @Last modified time: 2019-10-03T07:27:36-04:00



#Programa para pedir valores por teclado
ip = raw_input("Ingrese una dirección IP para conectarse: ")
puerto = raw_input("Ingrese el numero de puerto: ")

if puerto == "21":
    print("Intentando conectar con la ip " + ip + " y puerto " + puerto)
    print("Exito. Conexión establecida")
elif puerto == "22":
    print("Intentando conectar con la ip " + ip + " y puerto " + puerto)
    print("Exito. Conexión establecida")
else:
    print("Intentando conectar con la ip " + ip + " y puerto " + puerto)
    print("Fallido. No se pudo conectar a esa IP o puerto")
