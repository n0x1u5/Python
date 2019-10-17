# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2019-10-16T10:09:54-04:00
# @Last modified by:   root
# @Last modified time: 2019-10-16T10:29:25-04:00

nota1=int(input("Ingrese primer nota: "))
nota2=int(input("Ingrese segunda nota: "))
nota3=int(input("Ingrese tercer nota: "))
nota4=int(input("Ingrese tercer nota: "))
nota5=int(input("Ingrese nota del trabajo: "))
nota6=int(input("Ingrese nota de comportamiento: "))
prom=(nota1+nota2+nota3+nota4+nota5)/5
prom = prom+nota6
if prom>=5:
    print("Promocionado")
else:
    if prom>=4:
        print("Me pensaré aprobarte")
    else:
        print("Suspendido")
