# -*- coding: utf-8 -*-

nombre=input("Ingrese su nombre: ")
print("La primera letra de tu nombre es: " + str(nombre[0]))
if nombre[0]=="A" or nombre[0]=="E" or nombre[0]=="I" or nombre[0]=="O" or nombre[0]=="U":
    print("Tu nombre empieza por vocal")
else:
    print("Tu nombre empieza por consonante")
    
print("Tu nombre tiene " + str(len(nombre)) + " caracteres")