'''
Created on 23/07/2014

@author: thinktic
'''
import tkinter
from Fichero import *

def mostar(ev=None):
    fichero = Fichero ("agenda.csv")
    l = fichero.leer()
    resultado = tkinter.Label(top, text=l)
    resultado.pack()

top = tkinter.Tk()
top.geometry('250x150')

hello = tkinter.Label(top, text='Menu')
hello.pack()

label = tkinter.Label(top, text='Pulsa una opcion', font='Helvetica -12 bold')
label.pack()

mostar = tkinter.Button(top, text='Mostar', command=mostar, bg='red', fg='white')
mostar.pack()



quit = tkinter.Button(top, text='Salir', command=top.quit, activeforeground='white',
              activebackground='red')
quit.pack()

tkinter.mainloop()
