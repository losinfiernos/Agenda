# -*- coding: utf-8 -*-
'''
Created on: 2014/07/23

@author: jortegui
'''

import mysql.connector as dbapi


class Base_de_datos(object):

    def __init__(self, username, password, host, bbdd):
        self.username = username
        self.password = password
        self.host = host
        self.bbdd = bbdd
        self.conexion = dbapi.connect(user=self.username,
        password=self.password, host=self.host, db=self.bbdd)

    def insertar_contacto(self, nombre, apellido1, apellido2, email, anyos):
        self.cursor = self.conexion.cursor()
        self.query = "insert into contatos values(?, ?, ?, ?; ?)"
        self.cursor.execute(self.query, (nombre, apellido1, apellido2,
        email, anyos))
        self.conexion.commit()
        self.cursor.close()

    def devolver_contactos(self):
        self.cursor = self.conexion.cursor()
        self.query = "select * from alumnos"
        self.cursor.execute(self.query)
        self.contactos = []
        for self.i in self.cursor:
            self.contactos.append(self.i)
        self.cursor.close()
        return self.contactos

    def borrar(self,ident):
        self.cursor = self.conexion.cursor()
        self.query = "delete from alumnos where idalumnos = %i" %(ident)
        self.cursor.execute(self.query)
        self.conexion.commit()
        self.cursor.close()

    def alta(self, contacto):
        nombre = contacto.nombre
        apellido1 = contacto.apellido1
        apellido2 = contacto.apellido2
        email = contacto.email
        anyos = contacto.anyos
        self.cursor = self.conexion.cursor()
        self.query = "insert into alumnos (nombre, apellido1, apellido2, email, anyos) values ('%s', '%s', '%s', '%s', %i)" %(nombre, apellido1, apellido2, email, anyos)
        print (self.query)
        self.cursor.execute(self.query)
        self.conexion.commit()
        self.cursor.close()
