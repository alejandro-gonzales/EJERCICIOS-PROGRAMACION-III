class Condominio:
    def __init__(self):
        self.codigo = []
        self.departamento = []
        self.piso = []
        self.dimension = []
        self.ocupado = []
        self.tipoArrendamiento = []
        self.precioAlquiler = []
        self.precioVenta = []
        self.precioAnticretico = []
    
    def verificarNumero(self, valor):
        if valor.isdigit():
            return True
        else:
            return False

    def menu(self):
        opciones = """
        *****MENU DEL SISTEMA*****
        1.- Registrar
        2.- Ver Kardex
        3.- Ver Departamentos Disponibles
        4.- Ver Precio Venta
        5.- Ver Precio Anticretico
        6.- Ver Precio Alquiler
        7.- Ver Kardex Ascendente
        8.- Ver Kardex Descendente
        9.- Salir
        """
        print(opciones)

        valor = input("Selecciona una opcion: ")

        if self.verificarNumero(valor):
            eleccion = int(valor)
        else:
            print("Seleccione la opcion numerica correcta..!!")
            self.menu()

        if (eleccion == 1):
            self.agregarDpto()
            self.volverMenu()
        elif (eleccion == 2):
            self.listarDpto()
            self.volverMenu()
        elif (eleccion == 3):
            #self.verDptoDisponibles()
            self.volverMenu()
        elif (eleccion == 4):
            #self.verPrecioVenta()
            self.volverMenu()
        elif (eleccion == 5):
            #self.verPrecioAnticretico()
            self.volverMenu()
        elif (eleccion == 6):
            #self.verPrecioAlquiler()
            self.volverMenu()
        elif (eleccion == 7):
            self.verKardexAscendente()
            self.volverMenu()
        elif (eleccion == 8):
            self.verKardexDescendente()
            self.volverMenu()
        elif (eleccion == 9):
            print ("Gracias por Utilizar el Sistema")
        else:
            print("Seleccione una opcion Correcta")
            self.menu()
        pass
    
    def verKardexAscendente(self):
        #22, 25, 23, 24: #22, 23, 24, 25: #25, 24, 23, 22:
        #for i in range(len(self.departamento)):
        #dpto = [22, 25, 23, 24]
        #print(sorted(dpto))
        self.kardexOrdenado(False)

    def kardexOrdenado(self, orden):
        listaDpto = []
        for i in self.departamento:
            listaDpto.append(i)
        
        listaDpto.sort(reverse=orden)
        for i in range(len(listaDpto)):
            valor = listaDpto[i]
            posicion = self.departamento.index(valor)
            self.detalle(posicion)
            pass

    def verKardexDescendente(self):
        self.kardexOrdenado(True)

    def volverMenu(self):
        eleccion = input("Desea volver al Menu? s/n: ")
        if (eleccion == "s" or eleccion == "S"):
            self.menu()
        else:
            return "Gracias por Utilizar el Sistema"

    def obtenerCodTipoArrendamiento(self, v_tipo_arrendamiento):
        if(v_tipo_arrendamiento == "AL" or v_tipo_arrendamiento == "al"):
            return 1
        elif(v_tipo_arrendamiento == "VEN" or v_tipo_arrendamiento == "ven"):
            return 2
        elif(v_tipo_arrendamiento == "ANT" or v_tipo_arrendamiento == "ant"):
            return 3

    def obtenerCodOcupado(self, v_ocupado):
        if(v_ocupado == "S" or v_ocupado == "s"):
            return 1
        elif(v_ocupado == "N" or v_ocupado == "n"):
            return 0

    def obtenerValorOcupado(self, ocupado):
        if (ocupado == 1):
            return "Si"
        elif (ocupado == 0):
            return "No"
    
    def obtenerValorArrendamiento(self, tipoArrendamiento):
        if (tipoArrendamiento == 0):
            return "Disponible"
        elif (tipoArrendamiento == 1):
            return "Alquiler"
        elif (tipoArrendamiento == 2):
            return "Venta"
        elif (tipoArrendamiento == 3):
            return "Anticretico"
        
    def validarFormularioNumerico(self, valor):
        campo = input("Ingrese el Numero del {}: ".format(valor))
        if campo.isdigit():
            return int(campo)
        else:
            print("Debe Ingresar un Valor Numerico..!!")
            return self.validarFormularioNumerico(valor)

    def validarSiNo(self, mensaje):
        valor = input("{} s/n: ".format(mensaje))
        if (valor == "s" or valor == "S" or valor == "n" or valor == "N"):
            return valor
        else:
            print("Alerta, debe seleccionar si esta ocupado..!!")
            return self.validarSiNo(mensaje)

    def agregarDpto(self):
        departamento = self.validarFormularioNumerico("Dpto")
        piso = self.validarFormularioNumerico("Piso")
        dimension = self.validarFormularioNumerico("Dimension")
        v_ocupado = self.validarSiNo("Seleccion si esta ocupado")
        
        ocupado = self.obtenerCodOcupado(v_ocupado)
        if(ocupado == 1):
            v_tipo_arrendamiento = input("Seleccion el Tipo de Arrendamiento Al/Ven/Ant: ")
            tipo_arrendamiento = self.obtenerCodTipoArrendamiento(v_tipo_arrendamiento)
        elif(ocupado == 0):
            tipo_arrendamiento = 0  

        p_al = self.validarFormularioNumerico("Precio de Alquiler en $us")
        p_v = self.validarFormularioNumerico("Precio de Venta en $us")
        p_an = self.validarFormularioNumerico("Precio de Anticretico en $us")
        self.guardarDpto(departamento, piso, dimension, ocupado, tipo_arrendamiento, p_al, p_v, p_an)
        
        agregarMas = input("Desea Registrar mas Departamentos? s/n: ")
        
        if (agregarMas == "S" or agregarMas == "s"):
            self.agregarDpto()
        return "Departamentos Registrados Correctamente"

    def guardarDpto(self, dpto, piso, dim, ocupado, t_a, p_al, p_v, p_an):
        cod = "{}-{}".format(piso, dpto)
        self.codigo.append(cod)
        self.departamento.append(dpto)
        self.piso.append(piso)
        self.dimension.append(dim)
        self.ocupado.append(ocupado)
        self.tipoArrendamiento.append(t_a)
        self.precioAlquiler.append(p_al)
        self.precioVenta.append(p_v)
        self.precioAnticretico.append(p_an)
        self.listarDpto()
        return "El Departamento {} fue Registrado con el Codigo {} Exitosamente".format(dpto, cod)

    def listarDpto(self):
        for posicion in range(len(self.departamento)):
            self.detalle(posicion)
        pass

    def detalle(self, posicion):
        print("*******DEPARTAMENTO {}*******".format(self.codigo[posicion]))
        print("Numero de Departamento: {}".format(self.departamento[posicion]))
        print("Numero de Piso: {}".format(self.piso[posicion]))
        print("Dimension en m2: {}".format(self.dimension[posicion]))
        valorOcupado = self.obtenerValorOcupado(self.ocupado[posicion])
        print("Ocupado: {}".format(valorOcupado))
        valorTipoArrendamiento = self.obtenerValorArrendamiento(self.tipoArrendamiento[posicion])
        print("Tipo de Arrendamiento: {}".format(valorTipoArrendamiento))
        print("Precio de Alquiler: {}".format(self.precioAlquiler[posicion]))
        print("Precio de Anticretico: {}".format(self.precioAnticretico[posicion]))
        print("Precio de Venta: {}".format(self.precioVenta[posicion]))
        print("-----------------------------------------------------")
        pass


condominio = Condominio()
condominio.guardarDpto(22, 3, 48, 1, 1, 220, 12000, 2400000)
condominio.guardarDpto(25, 4, 48, 0, 1, 250, 12000, 2400000)
condominio.guardarDpto(23, 2, 48, 0, 1, 230, 12000, 2400000)
condominio.guardarDpto(24, 1, 48, 1, 1, 240, 12000, 2400000)
condominio.menu()

#CONDOMINIO DE 60 DPTOS. DE 5 PISOS, EN CADA PISO EXISTEN 12 DPTO., 1-1, 1-12
#DPTO 2-13, 2-24