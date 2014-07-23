'''
Created on 22/07/2014

@author: thinktic
'''
class Fichero(object):

    def __init__(self,nombrefichero):
        self.nombre = nombrefichero

    def leer(self):
        f = open(self.nombre, 'r')
        while True:
            linea = f.readline()
            print(linea)
            l = linea.split(",")
            if not linea:
                break
        return l