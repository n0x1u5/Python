# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2019-10-16T10:09:54-04:00
# @Last modified by:   root
# @Last modified time: 2019-10-16T10:44:55-04:00

totalpreguntas=int(input("Ingrese la cantidad total de preguntas del examen:"))
totalcorrectas=int(input("Ingrese la cantidad total de preguntas contestadas correctamente:"))
porcentaje=totalcorrectas * 100 / totalpreguntas
if porcentaje>=90:
    print("Nivel máximo")
else:
    if porcentaje>=75:
        print("Nivel medio")
    else:
        if porcentaje>=50:
            print("Nivel regular")
        else:
            print("Fuera de nivel")
