class Producto:
    def __init__(self):
        self.codigo = []
        self.nombre = []
        self.precio_compra = []
        self.precio_venta = []
        self.fabricacion = []
        self.vencimiento = []
        self.proveedor = []
        self.estado = []

    def menu(self):
        opciones = """
        1.- AGREGAR PRODUCTO
        2.- MOSTRAR INVENTARIO
        3.- ACTUALIZAR PRECIO DE VENTA
        4.- TIEMPO DE VIGENCIA DE PRODUCTO
        5.- TIEMPO DE VALIDEZ DEL PRODUCTO
        6.- ELIMINAR PRODUCTO
        7.- DAR DE ALTA EL PRODUCTO
        8.- DAR DE BAJA EL PRODUCTO
        9.- MOSTRAR INVENTARIO DE BAJA
        10.- SALIR
        """
        print(opciones)
        seleccionar = input("Seleccionar una opcion: ")
        
        if (seleccionar == "1"):
            print(self.agregarProducto())
            self.menu()
        
        elif (seleccionar == "2"):
            print(self.verInventarioAlta())
            print(self.volverMenu())
        
        elif (seleccionar == "3"):
            print(self.editarPrecioVenta())
            print(self.volverMenu())
        
        elif (seleccionar == "4"):
            pass
            self.menu()
        
        elif (seleccionar == "5"):
            pass
            self.menu()
        
        elif (seleccionar == "6"):
            print(self.realizarEliminacion())
            print(self.volverMenu())

        elif (seleccionar == "7"):
            print(self.realizarAlta())
            print(self.volverMenu())
        
        elif (seleccionar == "8"):
            print(self.realizarBaja())
            print(self.volverMenu())

        elif (seleccionar == "9"):
            print(self.verInventarioBaja())
            print(self.volverMenu())
        
        elif (seleccionar == "10"):
            print("Transacciones realizadas Exitosamente")

        else:
            print("Seleccionar una opcion del Menu..!!")
            self.menu()

    def agregarProducto(self):
        codigo = input("Codigo del Producto: ")
        nombre = input("Nombre del Producto: ")
        precio_compra = int(input("Precio de Compra: "))
        fecha_fabricacion = input("Fecha de Fabricacion: ")
        fecha_vencimiento = input("Fecha de Vencimiento: ")
        proveedor = input("Proveedor: ")
        
        self.guardarProducto(codigo, nombre, precio_compra, fecha_fabricacion, fecha_vencimiento, proveedor)

        agregarOtro = input("Desea Agregar otro Producto: y/n \n")

        if (agregarOtro == "y" or agregarOtro == "Y"):
            self.agregarProducto()
        return "Productos Agregados Correctamente!"

    def guardarProducto(self, codigo, nombre, precioCompra, fechaFabricacion, fechaVencimiento, proveedor):
        self.codigo.append(codigo)
        self.nombre.append(nombre)
        self.precio_compra.append(precioCompra)
        self.precio_venta.append((precioCompra * 0.4) + precioCompra)
        self.fabricacion.append(fechaFabricacion)
        self.vencimiento.append(fechaVencimiento)
        self.proveedor.append(proveedor)
        self.estado.append(1)
        return "Producto {} Agregados Correctamente!".format(nombre)

    def verInventarioAlta(self):
        return self.inventario(1)

    def verInventarioBaja(self):
        return self.inventario(0)

    def inventario(self, estado):
        if (self.nombre):
            for i in range (len(self.nombre)):
                self.descripcion(i, estado)
            return "Inventario cargado Correctamente"
        else:
            return "********TODAVIA NO SE AGREGARON PRODUCTOS A LA BASE DE DATOS********"

    def descripcion(self, posicion, estado):
        if (self.estado[posicion] == estado):
            print("******************DESCRIPCION DEL PRODUCTO {} ******************".format(self.nombre[posicion]))
            print("CODIGO DE PRODUCTO: {} Bs.".format(self.codigo[posicion]))
            print("PRECIO DE COMPRA: {} Bs.".format(self.precio_compra[posicion]))
            print("PRECIO DE VENTA: {} Bs.".format(self.precio_venta[posicion]))
            print("FECHA DE FABRICACION: {}".format(self.fabricacion[posicion]))
            print("FECHA DE VENCIMIENTO: {}".format(self.vencimiento[posicion]))
            print("PROVEEDOR: {}".format(self.proveedor[posicion]))
            print("ESTADO: {}".format(self.estado[posicion]))
            print("*******************************************************************")
            pass

    def editarPrecioVenta(self):
        print("***************ACTUALIZAR PRECIO DE VENTA***************")
        posicion = self.buscarProducto(1)
        self.descripcion(posicion, 1)
        nuevo_precio = input("Digite el nuevo precio de Venta del Producto {}: ".format(self.nombre[posicion]))
        print(self.modificarPrecioVenta(posicion, nuevo_precio))
        self.descripcion(posicion, 1)
        return "****************************Modificacion de Precio de Venta Completado****************************"

    def modificarPrecioVenta(self, posicion, pvn):
        self.precio_venta[posicion] = pvn
        return "Precio de Venta del Producto {} modificado correctamente".format(self.nombre[posicion])

    def volverMenu(self):
        eleccion = input("Desea volver al Menu? y/n: ")
        if (eleccion == "y" or eleccion == "Y"):
            self.menu()
        else:
            return "--------TRANSACCIONES TERMINADAS--------"

    def realizarEliminacion(self):
        print("**********SELECCIONAR EL PROPDUCTO A ELIMINAR**********")
        posicion = self.buscarProducto(1)
        return self.eliminar(posicion)

    def buscarProducto(self, estado):
        print(self.inventario(estado))
        eleccion = input("Digite el Codigo del Producto a Eliminar: ")
        posicion = self.codigo.index(eleccion)
        return posicion

    def eliminar(self, posicion):
        cod = self.codigo[posicion]
        self.codigo.pop(posicion)
        self.nombre.pop(posicion)
        self.precio_compra.pop(posicion)
        self.precio_venta.pop(posicion)
        self.fabricacion.pop(posicion)
        self.vencimiento.pop(posicion)
        self.proveedor.pop(posicion)
        self.estado.pop(posicion)
        return "Eliminacion Realizada del Producto {}".format(cod)

    def realizarAlta(self):
        print("**********DAR ALTA UN PRODUCTO**********")
        posicion = self.buscarProducto(0)
        return self.darAlta(posicion)
    
    def realizarBaja(self):
        print("**********DAR BAJA UN PRODUCTO**********")
        posicion = self.buscarProducto(1)
        return self.darBaja(posicion)

    def darAlta(self, posicion):
        self.estado[posicion] = 1
        return "El Producto {} esta de Alta..!!".format(self.nombre[posicion])

    def darBaja(self, posicion):
        self.estado[posicion] = 0
        return "El Producto {} esta de Baja..!!".format(self.nombre[posicion])



productos = Producto()
productos.guardarProducto("A101", "CAFE", 4, "21-05-2020", "21-05-2021", "NESCAFE")
productos.guardarProducto("A102", "AZUCAR", 8, "21-05-2020", "21-05-2021", "PELE")
productos.guardarProducto("A103", "LECHE", 10, "21-05-2020", "21-05-2021", "PIL")
productos.menu()





