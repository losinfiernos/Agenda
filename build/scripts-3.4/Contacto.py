class Contacto(object):

    def __init__(self, nombre, apellido1, apellido2, email, anyos):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.email = email
        self.anyos = anyos

    def getContact(self):
        return[self.nombre, self.apellido1, self.apellido2, self.email,
        self.anyos]





