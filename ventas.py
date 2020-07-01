class Ventas:
    def __init__(self, p_cliente):
        self.cliente = p_cliente
        self.productos = []
        self.precios = []

    def registroCliente(self):
        print("Bienvenido {} elije las Opciones del Menu:".format(self.cliente))
        menu = input("""
        1.- Comprar
        2.- Total a Cancelar
        
        Elegiste la Opcion: """)
        if(menu == "1"):
            self.registroCompra()
        elif(menu == "2"):
            self.compraTotal()
        else:
            return print("Elija la opcion Correcta")
    
    def registroCompra(self):
        print("************************************************")
        rProdructo = input("Digite el Producto a Comprar: ")
        self.productos.append(rProdructo)
        rPrecio = int(input("Ingrese el Precio de {}: ".format(rProdructo)))
        self.precios.append(rPrecio)
        print("{} {} Bs. Registrado Correctamente.!".format(rProdructo, rPrecio))
        pAdicional = input("Desea Registrar otro Producto? y/n: ")
        if(pAdicional == "y"):
            self.registroCompra()
        elif (pAdicional == "n"):
            print("Productos Registrados Correctamente...!")
            print("************************************************")
            self.registroCliente()
        else:
            print ("Elija la opcion correcta: y/n")
            print("************************************************")
            return self.registroCliente()

        
    
    def compraTotal(self):
        print("****************COMPRA TOTAL****************")
        print("PRODUCTOS               PRECIO")
        for i in range (len(self.productos)):
            print(self.productos[i], "            ", self.precios[i], " Bs.")
        print("************************************************")
        
        total = 0
        for t in self.precios:
            total = total + t
        print("El Total  a pagar es : {} Bs.".format(total))
        print("************************************************")

alejandro = Ventas("Alejandro Gonzales")


print(alejandro.registroCliente())



