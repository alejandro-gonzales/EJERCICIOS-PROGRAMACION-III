class Tienda:
    def __init__(self):
        self.nombre = []
        self.descripcion = []
        self.direccion = []
        self.categoria = []
        self.estado = []

    def verificarNumero(self, dato):
        
        if dato.isdigit():
            return True
        else:
            return False

    def menu(self):
        opciones = """
        *********MENU DEL SISTEMA*********
        1.- AGREGAR TIENDA
        2.- MOSTRAR TODAS LAS TIENDAS
        3.- BUSCAR TIENDAS POR CATEGORIA
        4.- ACTUALIZAR PRODUCTOS DE TIENDA
        """
        print(opciones)
        dato = input("Elija una opcion: ")
        if self.verificarNumero(dato):
            eleccion = int(dato)
        else:
            print("Debe digitar solo numeros..!!")
            self.menu()

        self.opciones(eleccion)

    def opciones(self, eleccion):
        if (eleccion == 1):
            print(self.agregarTienda())
            self.menu()
        elif (eleccion == 2):
            self.mostrar()
            self.menu()
        elif (eleccion == 3):
            self.usuarioBuscar()
            self.menu()
        elif (eleccion == 4):
            self.actualizarDescripcion()
            self.menu()
        elif (eleccion == 5):
            print("Transacciones realizadas")
        else:
            print("Elija una opcion del Menu")
            self.menu()

    def agregarTienda(self):
        nombre = input("Digite el nombre de la Tienda: ")
        descripcion = input("Digite la Descripcion: ")
        direccion = input("Digite la direccion: ")
        categoria = input("Digite la categoria: ")
        print(self.guardarTienda(nombre, descripcion, direccion, categoria))
        agregarOtro = input("Desea registrar mas Tiendas? s/n: ")
        if (agregarOtro == "s" or agregarOtro == "S"):
            self.agregarTienda()
        return "Tiendas Agregadas Exitosamente"
    
    def guardarTienda(self, nombre, descripcion, direccion, categoria):
        self.nombre.append(nombre)
        self.descripcion.append(descripcion)
        self.direccion.append(direccion)
        self.categoria.append(categoria)
        self.estado.append(1)
        return "Tienda {} registrada correctamente.!".format(nombre)
        
    def mostrar(self):
        for i in range(len(self.categoria)):
            self.detalle(i)
        pass

    def detalle(self, posicion):
        print("*********TIENDA {}*********".format(self.nombre[posicion]))
        print("Productos: {}".format(self.descripcion[posicion]))
        print("Direccion: {}".format(self.direccion[posicion]))
        print("Categoria: {}".format(self.categoria[posicion]))
        pass
    
    def usuarioBuscar(self):
        categoria = input("Escriba la Categoria a Buscar: ")
        return self.buscarCategoria(categoria)
    
    def buscarCategoria(self, categoria):
        encontrado = False
        for i in range(len(self.nombre)):
            if (self.categoria[i] == categoria):
                encontrado = True
                self.detalle(i)
        if (encontrado == False):
            print("No se encontraron Resultados con la Categoria {}".format(categoria))
        pass

    def verTienda(self):
        posicion = int(input("Digite la Posicion: "))
        self.detalle(posicion - 1)
        pass
    
    def actualizarDescripcion(self):
        posicion = self.usuarioBuscarTienda()
        descripcionActual = self.descripcion[posicion]
        descripcionNueva = input("Agregar datos a la Descripcion {} :".format(descripcionActual))
        descripcionActualizada = descripcionActual + " " + descripcionNueva
        return self.guardarActDesc(descripcionActualizada, posicion)

    def guardarActDesc(self, descripcion, posicion):
        self.descripcion[posicion] = descripcion
        return "Tienda Actualizada Exitosamente..!!"

    def usuarioBuscarTienda(self):
        tienda = input("Digite el Nombre de la Tienda: ")
        posicion = self.nombre.index(tienda)
        self.detalle(posicion)
        return posicion

    def buscarTienda(self, tienda):
        encontrado = False
        for i in range(len(self.nombre)):
            if (self.nombre[i] == tienda):
                encontrado = True
                self.detalle(i)
        if (encontrado == False):
            print("No se encontro la Tienda {} ".format(tienda))
        pass

tiendas = Tienda()
tiendas.guardarTienda("Pollos Kiky", "Cuarto de Pollo 15 Bs.", "Doble Via La Guardia 5to Anillo", "Restaurant")
tiendas.guardarTienda("Centro Informatico", "Tv Box Xiaomi 500 Bs.", "Comercial Neval #42", "Electronica")
tiendas.guardarTienda("El Tren Rojo", "Hamburguesas 12 Bs.", "2do Anillo", "Restaurant")
tiendas.guardarTienda("Ferreteria San Jorge", "Fierro de 2 Pulg.", "Doble Via La Guardia 6to Anillo", "Ferreteria")
tiendas.menu()




