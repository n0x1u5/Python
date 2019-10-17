# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2019-10-09T11:22:58-04:00
# @Last modified by:   root
# @Last modified time: 2019-10-16T10:09:28-04:00



#Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro del mismo (El perímetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)

num1 = int (input("Intruduce el lado del cuadrado: "))
calculo = num1*6
print("El resultado es: " + str(calculo))

#Escribir un programa en el cual se ingresen cuatro números, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto.

num1 = int(input("Intruduce un numero: "))
num2 = int(input("Intruduce otro numero: "))
num3 = int(input("Intruduce otro numero: "))
num4 = int(input("Intruduce otro numero: "))
suma = num1+num2
multiplicacion = num3*num4
print("La suma de " + num1 " y " + num2 " es: " + str(suma))
print("La multiplicacion de " + num3 " y " + num4 " es: " + str(multiplicacion))
