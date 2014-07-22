# -*- coding: utf-8 -*-


class Terminal(object):

    def imprimir_contacto(self, contacto):
        print ("Nombre: ", contacto.nombre)
        print (("Apellidos: ", contacto.apellido1, contacto.apellido2))
        print ("e-mail: ", contacto.email)
        print ("Años trabajados: ", contacto.anyos)

    def mostar_menu(self, opciones):
        for i in range(len(opciones - 1)):
            print("Opción", i, ":", opciones[i])
        choice = input("Introduce una de las opciones")
        return choice


