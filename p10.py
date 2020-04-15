# @Author: root
# @Date:   2019-09-24T04:24:18-04:00
# @Last modified by:   root
# @Last modified time: 2019-09-24T05:39:25-04:00
# -*- coding: utf-8 -*-


print("Indique una de estas opciones ")
print("======================================")
print("A) Mostrar numeros del 1 al 100 de uno en uno")
print("B) Mostrar numeros del 1 al 100 de dos en dos(pares)")
print("C) Mostrar numeros del 1 al 100 de tres en tres")
seleccion=input("Seleccion: ")
if seleccion == "A":
    for x in range(101):
        print(x)
        x=x+1
elif seleccion == "B":
    for x in range(0,101,2):
        print(x)
elif seleccion == "C":
    for x in range(0,101,3):
        print(x)
else:
    print("Indique una opción válida (A,B,C)...Saliendo")
    