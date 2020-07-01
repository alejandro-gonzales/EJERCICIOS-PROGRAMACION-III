class Persona:
    def __init__(self, nombre, apellido, genero, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.telefono = telefono
    
    def saludar(self):
        return "Hola.! Soy {} {}".format(self.nombre, self.apellido)

class Supervisor(Persona):
    def __init__(self, nombre, apellido, genero, telefono, area, profesion):
        Persona.__init__(self, nombre, apellido, genero, telefono)
        self.area = area
        self.profesion = profesion
    
    def mostrarArea(self):
        return "Soy el Supervisor {} y estoy encargado del area de {}".format(self.nombre, self.area)

class Obrero(Persona):
    def __init__(self, nombre, apellido, genero, telefono, especialidad, area):
        Persona.__init__(self, nombre, apellido, genero, telefono)
        self.especialidad = especialidad
        self.area = area
    
    def presentarse(self):
        return "Hola soy {} mis habilidades son: {} y estoy en el area {}".format(self.nombre, self.especialidad, self.area)


obrero = Obrero("Pablo", "Mercado", "Masculino", "76052321", "Levantamiento de Muros Azulejos", "Contruccion")    


supervisorAlberto = Supervisor("Mario", "Mercado", "Masculino", "76052321", "Electricidad", "Ing. Electrico")

print(supervisorAlberto.saludar())
print(supervisorAlberto.mostrarArea())

#alberto = Persona("Alberto", "Mercado", "Masculino", "76052321")
#print(alberto.saludar())



