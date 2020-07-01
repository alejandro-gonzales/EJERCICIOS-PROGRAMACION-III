class Estudiante():
    def __init__(self, p_nombre, p_apellido, p_carrera, p_materia):
        self.nombre = p_nombre
        self.apellido = p_apellido
        self.carrera = p_carrera
        self.materia = p_materia
        self.estado = 1
    
    def saludar(self):
        return "Hola Soy %s, Mucho Gusto." %(self.nombre)

    def materiaEstudiante(self):
        return "Hola Soy %s y estoy cursando la materia de %s" %(self.nombre, self.materia)

    def carreraEstudiante(self):
        return "Hola Soy %s %s y estoy en la Carrera de %s" %(self.nombre, self.apellido, self.carrera)

juan = Estudiante("Juan", "Perez", "Ing. de Sistemas", "Programacion I")
maria = Estudiante("Maria", "Cubillo", "Ing. Comercial", "Calculo I")

print(juan.saludar())
print(maria.saludar())

print("***********************************************")

print(juan.materiaEstudiante())
print(maria.materiaEstudiante())

print("***********************************************")

print(juan.carreraEstudiante())
print(maria.carreraEstudiante())
    

