def insertion_sort(A):
    Longitud = len(A)
    
    i = 1
    while i < Longitud:
        current = A[i] #Guarda el elemento actual
        j = i - 1 # Comparar el valor de "code" en lugar de index 1
        while j >= 0 and A[j]["code"] > current["code"]:
            A[j + 1] = A[j] #Mueve el elemento A[j] una posicion a la derecha
            j = j - 1 #Disminuye J para seguir buscando la posicion correcta de "current" a la izquierda
        A[j + 1] = current #El "current" lo mueve a la posicion correcta (A[j + 1])
        i = i + 1 #Avanza a la siguiente posicion

#Array a ordenar
A = [
    {"name": "Mariana", "code": 9},
    {"name": "Valentina", "code":5},
    {"name": "Isabella", "code": 7},
    {"name": "Sofía", "code": 3},
    {"name": "Juan", "code": 4},
    {"name": "Daniel", "code": 2},
    {"name": "Carlos", "code":6},
    {"name": "Camila", "code": 1},
    {"name": "Felipe","code": 10},
    {"name": "Andrés", "code": 8}
]

print(A)
print("")
insertion_sort(A)
print(A)