from models.pedido import Pedido
from models.producto import Producto

class PedidoBuilder:
    def __init__(self):
        self.pedido = Pedido()

    def agregar_cafe(self):
        self.pedido.agregar_producto(Producto("Café", 2.5))
        return self

    def agregar_te(self):
        self.pedido.agregar_producto(Producto("Té", 2.0))
        return self

    def agregar_medialuna(self):
        self.pedido.agregar_producto(Producto("Medialuna", 1.5))
        return self

    def agregar_sandwich(self):
        self.pedido.agregar_producto(Producto("Sándwich", 3.5))
        return self

    def construir(self):
        return self.pedido