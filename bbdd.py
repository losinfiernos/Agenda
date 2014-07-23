# -*- coding: utf-8 -*-
'''
Created on: 2014/07/23

@author: jortegui
'''

import mysql.connector as dbapi


class Base_de_datos(object):

    def __init__(self, username, password, bbdd):
        self.username = username
        self.password = password
        self.bbdd = bbdd
        self.conexion = dbapi.connect(user=self.username,
        password=self.password, db=self.bbdd)


