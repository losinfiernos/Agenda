
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

def mostarbdd (ev=None):
    l=[]
    bbdd = Base_de_datos('root', '', '127.0.0.1', 'agenda')
    l = bbdd.devolver_contactos()
    texto = ''
    for dato in l:
        texto = texto + ' ' + str(dato) + '\n'
    texto = texto + '\r\n' +'se han encontrado %i registros' %(len(l))
    resultado2 = Label(text=texto)
    resultado2.pack()

def borrar (ev=None):
    fichero = Fichero ("agenda.csv")
    fichero.borrar()

def borrar_bbdd (ev=None):
    ventana2 = Tk()
    ventana2.geometry("100x100+20+20")
    ventana2.title("Borrar bbdd")
    e = Entry (ventana2)
    e.pack()
    e.focus_set()

    def callback():
        ident = e.get()
        bbdd = Base_de_datos('root', '', '127.0.0.1', 'agenda')
        bbdd.borrar(int(ident))
        resultado = Label(text='Elemento borrado')
        resultado.pack()
        ventana2.withdraw()

    b = Button(ventana2, text='Borrar', command=callback)
    b.pack()
    ventana2.mainloop()


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
mnuArchivo.add_command(label="Listar los contactos en fichero",command = mostar)
mnuArchivo.add_command(label="Listar los contactos en BdD",command = mostarbdd)
mnuArchivo.add_command(label="Borrar primer dato fichero", command = borrar)
mnuArchivo.add_command(label="Borrar dato BdD", command = borrar_bbdd)
mnuArchivo.add_command(label="Buscar")
mnuArchivo.add_command(label="Dar de alta un nuevo contacto en BdD")
#Paso 4.- Agregar los menus a la barra de menus
barraMenu.add_cascade(label="Archivo",menu=mnuArchivo)
#Paso 5.- Indicamos que la barra de menus estará en la ventana
ventana.config(menu=barraMenu)
ventana.mainloop()


