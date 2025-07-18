class Pedido:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto):
        self.items.append(producto)

    def total(self):
        return sum(p.precio for p in self.items)

    def __str__(self):
        detalles = "\n".join(str(p) for p in self.items)
        return f"Pedido:\n{detalles}\nTotal: ${self.total():.2f}"
