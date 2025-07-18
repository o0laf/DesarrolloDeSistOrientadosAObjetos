from core.pedido_builder import PedidoBuilder
from core.cafeteria import Cafeteria

def mostrar_menu():
    print("\n--- MENÚ CAFETERÍA ---")
    print("1. Crear nuevo pedido")
    print("2. Ver pedidos")
    print("3. Salir")

def menu_pedido():
    builder = PedidoBuilder()
    while True:
        print("\n--- Crear Pedido ---")
        print("1. Agregar café")
        print("2. Agregar té")
        print("3. Agregar medialuna")
        print("4. Agregar sándwich")
        print("5. Finalizar pedido")
        opcion = input("Opción: ")
        if opcion == "1":
            builder.agregar_cafe()
        elif opcion == "2":
            builder.agregar_te()
        elif opcion == "3":
            builder.agregar_medialuna()
        elif opcion == "4":
            builder.agregar_sandwich()
        elif opcion == "5":
            return builder.construir()
        else:
            print("Opción inválida.")

def main():
    cafeteria = Cafeteria()

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")
        if opcion == "1":
            pedido = menu_pedido()
            cafeteria.agregar_pedido(pedido)
            print("\nPedido agregado con éxito!")
        elif opcion == "2":
            cafeteria.mostrar_pedidos()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()