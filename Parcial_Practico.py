import time

class RouteNode:
    #Nodo para representar cada ubicacion en la ruta
    def __init__(self, location):
        self.location = location
        self.next = None

class Route:
    def __init__(self):
        self.head = None  #La cabeza de la lista, que representa el inicio de la ruta

    def add_location(self, location):
        new_node = RouteNode(location)
        if not self.head:
            self.head = new_node  
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node

    def show_route(self):
        current = self.head
        if not current:
            print("⚠️ No hay una ruta definida.")
            return
        print("🛣️ Ruta definida:")
        while current is not None:
            print(f"➡️ {current.location}")
            current = current.next

    def navigate_route(self):
        current = self.head
        if not current:
            print("⚠️ No hay una ruta para navegar.")
            return

        print("🚗 Iniciando recorrido...")

        def show_next_step(node):
            if not node:
                print("🏁 Fin del recorrido.")
                return
            time.sleep(1.5)
            print(f"🛑 Llegaste a: {node.location}")
            show_next_step(node.next)

        show_next_step(current)


locations = [
    "Calle 5",
    "Avenida del Río",
    "Parque Sur",
    "Teatro Municipal",
    "Biblioteca Pública"
]

if __name__ == "__main__":
    city_route = Route()

    # Agregar rutas de manera iterativa dependiendo de si su último número del código es par o impar
    for location in locations:
        city_route.add_location(location)

    city_route.show_route()

    print("\n🔄 Simulación del recorrido en la ruta:\n")
    city_route.navigate_route()