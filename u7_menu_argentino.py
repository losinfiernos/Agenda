
#En la version 3 tkinter va con minusculas
from tkinter import *
from Fichero import *

def mostar(ev=None):
    fichero = Fichero ("agenda.csv")
    l = fichero.leer()
    texto = ''
    for dato in l:
        texto = texto + ' ' + dato
    texto = texto + '\r\n \r\n' +'se han encontrado %i registros' %(len(l)-1)
    resultado = Label(text=texto)
    resultado.pack()

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
mnuArchivo.add_command(label="Dar de alta un nuevo contacto")
mnuArchivo.add_command(label="Listar los contactos",command=mostar)
mnuArchivo.add_command(label="Buscar")
mnuArchivo.add_command(label="Borrar todos")
#Paso 4.- Agregar los menus a la barra de menus
barraMenu.add_cascade(label="Archivo",menu=mnuArchivo)
#Paso 5.- Indicamos que la barra de menus estará en la ventana
ventana.config(menu=barraMenu)
ventana.mainloop()


