# @Author: root
# @Date:   2019-10-03T10:25:03-04:00
# @Last modified by:   root
# @Last modified time: 2019-10-03T10:31:48-04:00


#Otra forma de tratar archivos
archivo = open("hoja1.txt","w+") #Abrimos el archivo para escribir
archivo.write("He escrito en el archivo\n")
archivo.write("otra vez\n")
archivo.write("otra vez\n")
archivo.write("otra vez\n")
archivo.write("otra vez\n")
with open("hoja1.txt", "r") as archivo:
    print archivo.read()
archivo.close()
