class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Cola:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return value

queue = Cola()
for num in [1, 2, 3, 4, 5]:
    queue.enqueue(num)

print(queue.dequeue())
print(queue.dequeue()) 
print(queue.dequeue()) 
print(queue.dequeue()) 
print(queue.dequeue()) 
print(queue.dequeue()) 