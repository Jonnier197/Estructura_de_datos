def linear (array, target):
    i = 0
    while i < len(array):
        if (array[i] == target):
            return i
        i = i + 1
    return -1
A = [10,1,5,4,7,9,11]
T = 11

linear(A,T)
print(linear(A,T))