# @Author: root
# @Date:   2019-10-01T09:32:34-04:00
# @Last modified by:   root
# @Last modified time: 2019-10-02T09:46:15-04:00


def ataqueFTP(ip):
    print("Atacando a la IP " + ip + " por FTP")

def ataqueSSH(ip):
    print("Atacando a la IP " + ip + " por SSH")

victimas = ["192.168.1.1","192.168.1.2"]
puertos = [21,22,23,80,443]

for victima in victimas:
    for puerto in puertos:
        if puerto == 21:
            ataqueFTP(victima)
        elif puerto == 22:
            ataqueSSH(victima)
        else:
            print ("No se reconce el puerto " + str(puerto) + " abierto")
