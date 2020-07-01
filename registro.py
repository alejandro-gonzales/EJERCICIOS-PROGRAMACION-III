class RegistroMateria:
    def __init__(self, p_estudiante, p_apellido, p_carrera):
        self.estudiante = p_estudiante
        self.apellido = p_apellido
        self.carrera = p_carrera
        self.materias = []
    
    def presentarse(self):
        print("*******Presentacion de %s %s*******" % (self.estudiante, self.apellido))
        for i in self.materias:
            print(i)

        return print("Soy el Estudiante: %s de la carrera de %s" % (self.estudiante, self.carrera))

    def registrarMateria(self):
        print("Gestion de Registro de Materias")
        materia = input("Digite la Materia: ")
        self.materias.append(materia)
        print("Materia %s registrada exitosamente.!" % (materia))
        adicional = input("Desea Registrar una Materia Adicional?: y/n: ")
        if (adicional == "y"):
            self.registrarMateria()
        else:
            return print("Materias Registradas Correctamente")

    def menu(self):
        opciones = """
        MENU DE LA APLICACION
        1.- Registrar Materias
        2.- Presentarse
        """
        print(opciones)
        eleccion = input("Elija una Opcion: ")
        if(eleccion == "1"):
            self.registrarMateria()
            self.menu()
        elif (eleccion == "2"):
            self.presentarse()
            self.menu()
        else:
            print("Elija una Opcion del Menu")
            self.menu()

jose = RegistroMateria("Jose", "Montaño", "Ing. de Sistemas")
pablo = RegistroMateria("Pablo", "Mercado", "Ing. Comercial")




print(jose.menu())