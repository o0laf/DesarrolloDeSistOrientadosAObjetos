class Cafeteria:
    __instancia = None

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
            cls.__instancia.pedidos = []
        return cls.__instancia

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def mostrar_pedidos(self):
        for i, pedido in enumerate(self.pedidos, 1):
            print(f"\nPedido {i}:\n{pedido}")
