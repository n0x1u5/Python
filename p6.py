# @Author: root
# @Date:   2019-10-07T06:20:57-04:00
# @Last modified by:   root
# @Last modified time: 2019-10-07T07:38:59-04:00

#Importamos libreria para poder usarla
import os

#Directorio actual. pwd
directorio = os.getcwd()
print(directorio)
print("============================")

#Listar directorios. ls.
lista1 = os.listdir('/var')
print(lista1)
print("============================")

#Crear y eliminar directorio
os.rmdir('prueba')
os.mkdir('prueba')
lista2 = os.listdir('.')
print(lista2)
print("============================")

#Crear y eliminar varios directorios
os.removedirs('prueba1/prueba2/prueba3')
os.makedirs('prueba1/prueba2/prueba3')
lista3 = os.listdir('/root/Documents/')
print(lista3)
print("============================")

#Crear y eliminar archivos
os.remove('hoja2.txt')
archivo = open("hoja2.txt","w+") #Se crea el archivo para escribir
archivo.write("He escrito en el archivo nuevo\n")
archivo.close()
lista4 = os.listdir('/root/Documents/')
print(lista4)
print("============================")
