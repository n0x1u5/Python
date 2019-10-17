# @Author: root
# @Date:   2019-10-07T09:14:21-04:00
# @Last modified by:   root
# @Last modified time: 2019-10-07T10:51:20-04:00



import os

dir = "/root/Documents"
for dirnombre, subdirectorio, listarchivo in os.walk(dir): #Se crean 3 variables, dirnombre para guardar la ruta de la que partimos "/root/Documents", subdirectorio para guardar cada uno de los directorios que hay a partir de "/root/Documents" y listarchivo para guardar el nombre del archivo
    print("Nombre de directorio: " + dirnombre)
    for archivo in listarchivo:
        print ("Archivo: " + archivo)
