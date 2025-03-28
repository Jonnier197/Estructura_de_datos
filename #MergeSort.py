#Funcion para ordenar por Merge Sort
def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, key)
        merge_sort(right, key)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][key] < right[j][key]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

#Funcion para ordenar por Heap Sort
def heapify(arr, n, i, key):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i][key] < arr[left][key]:
        largest = left
    if right < n and arr[largest][key] < arr[right][key]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)

#Funcion para ordenar por Quick Sort
def quick_sort(arr, low, high, key):
    if low < high:
        pi = partition(arr, low, high, key)
        quick_sort(arr, low, pi - 1, key)
        quick_sort(arr, pi + 1, high, key)

def partition(arr, low, high, key):
    pivot = arr[high][key]
    i = low - 1
    for j in range(low, high):
        if arr[j][key] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

#Funcion para buscar binariamente por edad o salario
def binary_search(arr, key, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][key] == value:
            return arr[mid]
        elif arr[mid][key] < value:
            low = mid + 1
        else:
            high = mid - 1
    return None

#Funcion para mostrar el menu interactivo
def mostrar_menu():
    print("Hola, bienvenido a mi aplicacion Empresarial, ¿Qué quieres hacer?:")
    print("1. Ordenar por edad")
    print("2. Ordenar por nombre")
    print("3. Ordenar por salario")
    print("4. Buscar por edad")
    print("5. Buscar por salario")

#Funcion principal
def main():
    empleados = [
        {"name": "Mariana", "code": 9, "age": 30, "salary": 5000},
        {"name": "Valentina", "code": 5, "age": 25, "salary": 4000},
        {"name": "Isabella", "code": 7, "age": 28, "salary": 4500},
        {"name": "Sofía", "code": 3, "age": 35, "salary": 5500},
        {"name": "Juan", "code": 4, "age": 26, "salary": 4200},
        {"name": "Daniel", "code": 2, "age": 40, "salary": 6000},
        {"name": "Carlos", "code": 6, "age": 29, "salary": 4700},
        {"name": "Camila", "code": 1, "age": 22, "salary": 3800},
        {"name": "Felipe", "code": 10, "age": 32, "salary": 5300},
        {"name": "Andrés", "code": 8, "age": 31, "salary": 5100}
    ]

    while True:
        mostrar_menu()
        option = input("Elige una opcion: ")

        if option == "1":
            key = "age"
            print("Ordenando por edad con Heap Sort...")
            heap_sort(empleados, key)
            for empleado in empleados:
                print(empleado)
        elif option == "2":
            key = "name"
            print("Ordenando por nombre con Quick Sort...")
            quick_sort(empleados, 0, len(empleados) - 1, key)
            for empleado in empleados:
                print(empleado)
        elif option == "3":
            key = "salary"
            print("Ordenando por salario con Merge Sort...")
            merge_sort(empleados, key)
            for empleado in empleados:
                print(empleado)
        elif option == "4":
            key = "age"
            value = int(input("Digite la edad a buscar: "))
            #Primero ordenamos por edad antes de realizar la busqueda
            empleados_ordenados = sorted(empleados, key=lambda x: x[key])  #Ordenamos por edad
            result = binary_search(empleados_ordenados, key, value)
            if result:
                print(f"Empleado encontrado: {result}")
            else:
                print("Empleado no encontrado.")
        elif option == "5":
            key = "salary"
            value = int(input("Introduce el salario a buscar: "))
            #Primero ordenamos por salario antes de realizar la busqueda
            empleados_ordenados = sorted(empleados, key=lambda x: x[key])  #Ordenamos por salario
            result = binary_search(empleados_ordenados, key, value)
            if result:
                print(f"Empleado encontrado: {result}")
            else:
                print("Empleado no encontrado.")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
