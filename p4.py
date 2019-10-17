# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2019-10-03T09:28:34-04:00
# @Last modified by:   root
# @Last modified time: 2019-10-03T10:24:33-04:00

#Manejo de archivos en python
archivo = open("hoja1.txt","w+") #Abrimos el archivo para escribir
print("Nombre de archivo: "),archivo.name
print("Modo de apertura: "),archivo.mode
archivo.write("He escrito en el archivo\n")
archivo = open("hoja1.txt","r") #Abrimos de nuevo el archivo para leer
contenido = archivo.read() #Guardamos su contenido en una variable
print contenido
archivo.close()
print("Cerrado: "),archivo.closed
