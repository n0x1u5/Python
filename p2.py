# @Author: root
# @Date:   2019-10-02T09:03:24-04:00
# @Last modified by:   root
# @Last modified time: 2019-10-03T09:26:53-04:00


class ataque: #Declaramos un objeto con tres funciones, init siempre será la primera
    def __init__(self, ip, puerto):
        self.ip = ip
        self.puerto = puerto
        #La palabra reservada self hace referencia a el mismo objeto, es decir, se llama a si mismo, esto significa que cuando llamamos a self.ip, recogemos lo que esta dentro de la variable ip en el programa de ejemplo.
    def FuerzaBrutaSSH(self):
        print 'SSH atacando al host ' + self.ip + ' puerto ' + str(self.puerto)

    def FuerzaBrutaFTP(self):
        print 'FTP atacando al host ' + self.ip + ' puerto ' + str(self.puerto)

atq = ataque("192.168.1.2",22) #Metemos el objeto en una variable para poder tratarla
atq.FuerzaBrutaSSH()
atq.puerto = 21
atq.FuerzaBrutaFTP()
atq.ip = "192.168.1.3"
atq.puerto = 22
atq.FuerzaBrutaSSH()
atq.puerto = 21
atq.FuerzaBrutaSSH()
#Ya podemos darle valor cuando queramos, con atq.variable = valor y para llamarla atq.funcion.
