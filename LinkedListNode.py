class LinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def LinkedListLookUp(head, element_number):
    current = head
    count = 0
    element_number -= 1
    
    while count < element_number and current is not None:
        current = current.next
        count += 1
    
    return current

def agregar_al_final(head, valor):
    new_node = LinkedListNode(valor)

    if head is None:
        return new_node
    
    current = head

    while current.next is not None:
        current = current.next
    
    current.next = new_node
    return head

def imprimir_lista(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

head = None

head = agregar_al_final(head, 10)
head = agregar_al_final(head, 20)
head = agregar_al_final(head, 30)
head = agregar_al_final(head, 40)
head = agregar_al_final(head, 50)

print("Lista enlazada:")
imprimir_lista(head)

element_number = 1
node = LinkedListLookUp(head, element_number)

if node:
    print(f"Elemento en la posición {element_number}: {node.value}")
else:
    print(f"No se encontró el elemento en la posición {element_number}")