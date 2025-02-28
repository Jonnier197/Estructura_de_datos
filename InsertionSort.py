def insertion_sort(A):
    Longitud = len(A)
    i = 1
    while i < Longitud:
        current = A[i]
        j = i - 1
        while j >= 0 and A[j] > current:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = current
        i = i + 1

#Array a ordenar
A = [10,1,5,4,7,9,11]
insertion_sort(A)
print(A)