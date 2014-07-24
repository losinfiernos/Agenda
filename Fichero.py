'''
Created on 22/07/2014

@author: thinktic
'''
class Fichero(object):

    def __init__(self,nombrefichero):
        self.nombre = nombrefichero

    def leer(self):
        l = []
        f = open(self.nombre, 'r')
        linea = f.readline()    #la primera linea con los campos la descarto
        while True:
            linea = f.readline()
            print(linea)
            l.append(linea)
            if not linea:
                break
        return l
        f.close()

    def borrar(self):
        f = open(self.nombre, 'r')
        linea = f.readline()    #la primera linea con los campos la descarto
        chain = linea
        f.readline()    #la segunda linea es el dato que borro
        while True:
            linea = f.readline()
            chain += linea
            #print(chain)
            if not linea:
                break
        f = open(self.nombre, 'w')
        f.write(chain)
        f.close()
        return ('registro borrado')