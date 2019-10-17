# @Author: root
# @Date:   2019-09-20T05:20:37-04:00
# @Last modified by:   root
# @Last modified time: 2019-09-23T11:17:43-04:00



fichero = open('hoja1.txt','r')
lineas = fichero.readlines()
fichero.close()

fichero_salida=open('salida_hoja1.txt','a')
siguiente=''
for x in lineas:

    if 'valorbin' in siguiente:
	fichero_salida.write(x.replace('\n','').replace('\r','')+";")
    if 'valorexp' in siguiente:
	fichero_salida.write(x.replace('\n','').replace('\r','')+";")
    if 'valorname' in siguiente:
	fichero_salida.write(x.replace('\n','').replace('\r','')+";")
    if 'valorcity' in siguiente:
	fichero_salida.write(x.replace('\n','').replace('\r','')+";")
    if 'valorzip' in siguiente:
	fichero_salida.write(x.replace('\n','').replace('\r','')+"\n")

    if 'BIN' in x:
        siguiente='valorbin'

    elif 'EXP' in x:
        siguiente='valorexp'
    elif 'NAME' in x:
        siguiente='valorname'
    elif 'CITY' in x:
        siguiente='valorcity'
    elif 'ZIP' in x:
        siguiente='valorzip'
    else:
        siguiente=''

fichero_salida.close()
