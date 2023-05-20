class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def obtener_producto_por_indice(self, indice):
        try:
            print(self.productos[indice]) 
        except IndexError:
            print('Está fuera de rango')

class Supermercado:
    def __init__(self):
        self.productos_valor = {
            'chocolate': 2500,
            'agua': 1000,
            'bebida': 2000
        }

    def consultar_valor(self, producto):
        try:
            print(self.productos_valor[producto]) 
        except KeyError:
            print(f"No se encontró el producto '{producto}'")



carro = CarritoCompras()
carro.agregar_producto('bebida')
carro.agregar_producto('chocolate')
carro.agregar_producto('agua')

carro.obtener_producto_por_indice(9)

lider = Supermercado()
lider.consultar_valor('cafe')

lider.calcular_descuento(15)

