# -*- coding: utf-8 -*-

opcion="Y"
suma=0
while opcion=="Y":
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    opcion=input("Desea cargar otro numero (Y/N):")
print("La suma de valores ingresados es: " + str(suma))