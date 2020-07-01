class Restaurante:
    def __init__(self):
        self.codigo = []
        self.nombre = []
        self.precio = []
        self.descripcion = []
        self.tipo = []
        self.habilitado = []
        self.descuento = []
    
    def verificarNumero(self, valor):
        if valor.isdigit():
            return True
        else:
            return False

    def menu(self):
        opciones = """
        **************MENU**************
        1.- REGISTRAR PLATO
        2.- MODIFICAR PLATO
        3.- MOSTRAR TODOS LOS PLATOS
        4.- MOSTRAR TIPOS DE PLATOS
        5.- MOSTRAR PLATOS DISPONIBLES
        6.- SALIR
        """
        print(opciones)

        seleccion = input("Ingrese el Numero de la Opcion: ")
        print("***********************************************")

        if self.verificarNumero(seleccion):
            seleccion = int(seleccion)
        else:
            print("Seleccione la opcion numerica correcta..!!")
            return self.menu()

        if(seleccion == 1):
            self.agregarPlatos()
            self.registrarOtroPlato()
        elif (seleccion == 2):
            self.actualizarPlato2()
            self.volverMenu()
        elif (seleccion == 3):
            self.cargarPlatos()
            self.volverMenu()
        elif (seleccion == 4):
            self.elegirTiposPlatos()
            self.volverMenu()
        elif (seleccion == 5):
            self.platosDisponibles()
            self.volverMenu()
        elif (seleccion == 6):
            print("Gracias por utilizar nuestro Servicio..!!")
        else:
            print("Elija un numero del Menu..!!")
            return self.menu()

    def volverMenu(self):
        volverM = input("Desea volver al Menu? S/N: ")
        if (volverM == "S" or volverM == "s"):
            self.menu()
        elif (volverM == "N" or volverM == "n"):
            print("Gracias por utilizar nuestro Servicio..!!")
        else:
            print("Introduzca las opciones validas S/N..!!")
            self.volverMenu()
    
    def elegirPlato(self):
        if (self.nombre):
            for posicion in range(len(self.nombre)):
                if (self.descuento[posicion] > 0):
                    print("Código: {}".format(self.codigo[posicion]))
                    print("Nombre: {} esta En OFERTA.!!".format(self.nombre[posicion]))
                    print("Habilitado: {}".format(self.habilitado[posicion]))
                    print("*******************************")
                else:
                    print("Código: {}".format(self.codigo[posicion]))
                    print("Nombre: {}".format(self.nombre[posicion]))
                    print("Habilitado: {}".format(self.habilitado[posicion]))
                    print("*******************************")
        else: 
            print("No hay platos Registrados")
        plato = int(input("Ingrese el Codigo del Plato: "))
        posicion = self.codigo.index(plato)
        self.mostrarPlatos(posicion)
        return posicion

    def actualizarPlato2(self):
        if (self.nombre):
            posicion = self.elegirPlato()
            opcion = """
            **************OPCIONES A MODIFICAR**************
            1.- Nombre
            2.- Precio
            3.- Descripcion
            4.- Tipo
            5.- Habilitado
            6.- Descuento
            """
            print(opcion)

            nombreNuevo = self.nombre[posicion]
            precioNuevo = self.precio[posicion]
            tipoNuevo = self.tipo[posicion]
            descripcionNuevo = self.descripcion[posicion]
            habilitadoNuevo = self.habilitado[posicion]
            descuentoNuevo = self.descuento[posicion]

            opcion = int(input("Elija el Numero de la Opcion Que quiere modificar: "))

            if (opcion == 1):
                nombreNuevo = input("Nuevo Nombre del Plato: ")
            elif (opcion == 2):
                precioNuevo = int(input("Nuevo Precio: "))
            elif (opcion == 3):
                descripcionNuevo = input("Nueva Descripcion: ")
            elif (opcion == 4):
                tipoNuevo = input("Nuevo Tipo de Plato: ")
            elif (opcion == 5):
                habilitadoNuevo = input("Esta Disponible? Si/No: ")
            elif (opcion == 6):
                descuentoNuevo = int(input("Nuevo Descuento: "))
            elif (opcion == 7):
                pass
            else:
                print("Elija un numero de opcion correcto..!!")
                self.actualizarPlato2()        
            return self.guardarActPlato(nombreNuevo, precioNuevo, descripcionNuevo, tipoNuevo, habilitadoNuevo, descuentoNuevo, posicion)
        else:
            return print("No hay Platos Disponibles para Modificar..!!")
        
    def guardarActPlato(self, nombreNuevo, precioNuevo, descripcionNuevo, tipoNuevo, habilitadoNuevo, descuentoNuevo, posicion):
        self.nombre[posicion] = nombreNuevo
        self.precio[posicion] = precioNuevo
        self.descripcion[posicion] = descripcionNuevo
        self.tipo[posicion] = tipoNuevo
        self.habilitado[posicion] = habilitadoNuevo
        self.descuento[posicion] = descuentoNuevo
        self.mostrarPlatos(posicion)        
        self.ActOtroPlato()

    def ActOtroPlato(self):    
        ActOtraCaracteristica = input("Desea cambiar otra Caracteristica de otro Plato? S/N: ")
        print("***********************************************")
        if (ActOtraCaracteristica == "S" or ActOtraCaracteristica == "s"):
            self.actualizarPlato2()
        elif (ActOtraCaracteristica == "N" or ActOtraCaracteristica == "n"):
            self.menu()
        return print("Plato Actualizado Exitosamente..!!")

    def cargarPlatos(self):
        if (self.nombre):
            for posicion in range(len(self.nombre)):
                self.mostrarPlatos(posicion)
            return print("**********Menu Cargado Correctamente**********")
        else:
            return print("No hay platos Registrados")
    
    def modificarOtroPlato(self):
        registrarOtro = input("Desea Modificar Otro Plato? S/N: ")
        print("***********************************************")
        if (registrarOtro == "S" or registrarOtro == "s"):
            self.actualizarPlato2()
            self.modificarOtroPlato()
        elif (registrarOtro == "N" or registrarOtro == "n"):
            self.menu()
        else:
            print("Elija un numero de opcion correcto..!!")
            self.modificarOtroPlato()

    def mostrarPlatos(self, posicion):
        if (self.nombre):
            if (self.descuento[posicion] > 0):
                desc = round(self.precio[posicion] - (self.precio[posicion] * (self.descuento[posicion]/100)),2)
                print("***********{} esta En OFERTA.!!***********".format(self.nombre[posicion]))
                print("Código: {}".format(self.codigo[posicion]))
                print("Descripcion: {}".format(self.descripcion[posicion]))
                print("Precio: {} Bs.".format(self.precio[posicion]))
                print("Descuento: {} %".format(self.descuento[posicion]))
                print("Precio con Descuento: {} Bs.".format(desc))
                print("Tipo: {}".format(self.tipo[posicion]))
                print("Habilitado: {}".format(self.habilitado[posicion]))
            else:
                print("***********{}***********".format(self.nombre[posicion]))
                print("Código: {}".format(self.codigo[posicion]))
                print("Descripcion: {}".format(self.descripcion[posicion]))
                print("Precio: {} Bs.".format(self.precio[posicion]))
                print("Tipo: {}".format(self.tipo[posicion]))
                print("Habilitado: {}".format(self.habilitado[posicion]))        
        else:
            return print("No hay platos Registrados")

    def elegirTiposPlatos(self):
        opcion = """
        **************TIPOS DE PLATOS**************
        1.- Desayuno
        2.- Almuerzo
        3.- Cena
        4.- Postre
        """
        print(opcion)

        opcion = int(input("Elija el Numero de la Opcion: "))

        if (opcion == 1):
            tipoPlato = "Desayuno"
        elif (opcion == 2):
            tipoPlato = "Almuerzo"
        elif (opcion == 3):
            tipoPlato = "Cena"
        elif (opcion == 4):
            tipoPlato = "Postre"
        else:
            print("Elija un numero de opcion correcto..!!")
            self.elegirTiposPlatos()
            
        return self.mostrarTiposPlatos(tipoPlato)
        
    
    def platosDisponibles(self):
        for posicion in range(len(self.nombre)):
            if (self.habilitado[posicion] == "Si"):
                self.mostrarPlatos(posicion)

    def mostrarTiposPlatos(self, tipoPlato):
        for posicion in range(len(self.nombre)):
            if (self.habilitado[posicion] == "Si"):
                if (self.tipo[posicion] == tipoPlato):
                        self.mostrarPlatos(posicion)

    
    def agregarPlatos(self):
        codigo = int(input("Ingrese el Codigo del Plato: "))
        nombre = input("Ingrese el Nombre del Plato: ")
        precio = int(input("Ingrese el Precio en Bolivianos: "))
        descripcion = input("Ingrese la Descripcion del Plato: ")
        tipo = input("Ingrese el Tipo de Plato.- (Desayuno, Almuerzo, Cena o Postre): ")
        habilitado = input("Esta habilitado el Plato Si/No: ")
        descuento = int(input("Ingrese el Descuento en Porcentaje: "))
        print("***********************************************")

        self.guardarPlatos(codigo, nombre, precio, descripcion, tipo, habilitado, descuento)
    
    def registrarOtroPlato(self):
        registrarOtro = input("Desea Registrar Otro Plato? S/N: ")
        print("***********************************************")
        if (registrarOtro == "S" or registrarOtro == "s"):
            self.agregarPlatos()
            self.registrarOtroPlato()
        elif (registrarOtro == "N" or registrarOtro == "n"):
            self.volverMenu()
        else:
            print("Elija un numero de opcion correcto..!!")
            self.registrarOtroPlato()

    def guardarPlatos(self, codigo, nombre, precio, descripcion, tipo, habilitado, descuento):
        self.codigo.append(codigo)
        self.nombre.append(nombre)
        self.precio.append(precio)
        self.descripcion.append(descripcion)
        self.tipo.append(tipo)
        self.habilitado.append(habilitado)
        self.descuento.append(descuento)
    
        
restaurant = Restaurante()
restaurant.guardarPlatos(1, "Empanadas de Queso", 3, "Empanadas fritas con mucho Queso", "Desayuno", "Si", 50)
restaurant.guardarPlatos(2, "Salteña", 8, "Salteña de Pollo", "Desayuno", "No", 0)
restaurant.guardarPlatos(3, "Ensalada de Frutas", 5, "Vaso Grande de Ensalada de Frutas", "Desayuno", "No", 0)
restaurant.guardarPlatos(4, "Majau", 10, "Majau de Charque", "Almuerzo", "Si", 20)
restaurant.guardarPlatos(5, "Sopa de Trigo", 5, "Sopa de Trigo con Chuño", "Almuerzo", "No", 0)
restaurant.guardarPlatos(6, "Chuleta", 12, "Chuleta de Res con Arroz y Ensalada", "Almuerzo", "Si", 0)
restaurant.guardarPlatos(7, "Pollo a la Broasted", 12, "Pollo a la broasted con Arroz y Papas Fritas", "Cena", "Si", 30)
restaurant.guardarPlatos(8, "Milaneza", 12, "Milaneza de Res con Arroz y Papas Fritas", "Cena", "Si", 0)
restaurant.guardarPlatos(9, "Hamburguesa", 15, "Hamburguesa de Res con Doble Queso y Papas Fritas", "Cena", "Si", 0)
restaurant.menu()

