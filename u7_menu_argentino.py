
#En la version 3 tkinter va con minusculas
from tkinter import *
from Fichero import *
from bbdd import *

def mostar(ev=None):
    fichero = Fichero ("agenda.csv")
    l = fichero.leer()
    texto = ''
    for dato in l:
        texto = texto + ' ' + dato
    texto = texto + '\r\n \r\n' +'se han encontrado %i registros' %(len(l)-1)
    resultado = Label(text=texto)
    resultado.pack()

def alta (ev=None):
    l=[]

def mostarbdd (ev=None):
    l=[]
    bbdd = Base_de_datos('root', '', '127.0.0.1', 'agenda')
    l = bbdd.devolver_contactos()
    texto = ''
    for dato in l:
        texto = texto + ' ' + str(dato) + '\n'
    texto = texto + '\r\n \r\n' +'se han encontrado %i registros' %(len(l)-1)
    resultado2 = Label(text=texto)
    resultado2.pack()


#crear una ventana
ventana = Tk()
ventana.geometry("600x600+0+0")
ventana.title("Ejemplo con Menús")
####RECETA PARA CREAR MENUS
#Paso 1. Crear la barra de menús
barraMenu = Menu(ventana)
#Paso 2.- Crear los menús
mnuArchivo = Menu(barraMenu)
#Paso 3.- Crear los comandos de los menus
mnuArchivo.add_command(label="Listar los contactos en fichero",command=mostar)
mnuArchivo.add_command(label="Listar los contactos en BdD",command=mostarbdd)
mnuArchivo.add_command(label="Borrar primer dato fichero")
mnuArchivo.add_command(label="Borrar primer dato BdD")
mnuArchivo.add_command(label="Buscar")
mnuArchivo.add_command(label="Dar de alta un nuevo contacto en BdD",
                       command=alta)
#Paso 4.- Agregar los menus a la barra de menus
barraMenu.add_cascade(label="Archivo",menu=mnuArchivo)
#Paso 5.- Indicamos que la barra de menus estará en la ventana
ventana.config(menu=barraMenu)
ventana.mainloop()


