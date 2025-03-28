class Stack:
    def __init__(self):
        self._items = [] 

    def push(self, item):
        "Agrega un elemento a la pila."
        self._items.append(item)

    def pop(self):
        "Elimina y devuelve el último elemento de la pila."
        return self._items.pop() if self._items else None

# Ejemplo de uso
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.pop())  # 5
print(stack.pop())  # 4
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.pop())  # None  (pila vacía)