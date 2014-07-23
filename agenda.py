'''
Created on 22/07/2014

@author: jecrespo
'''
from Contacto import *
from Fichero import *
from Terminal import *

#terminal = Terminal()
fichero = Fichero ("agenda.csv")
#contacto1 = Contacto("juan", "Perez", "Perez", "jpp@gmail.com", 6)
print(fichero.leer())
