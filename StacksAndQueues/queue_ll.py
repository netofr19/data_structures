class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        
        self._size += 1

    def dequeue(self):
        if self._size < 1:
            print("Queue is empty!")
            return None
        if self._size == 1:
            data = self.head.data
            self.head = None
            self.tail = None
            self._size -= 1
            return data
        if self._size > 1:
            data = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self._size -= 1
            return data
        
if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    current = queue.head
    print('[ ', end="")
    while current != None:
        print(current.data, end =", ")
        current = current.next
    print(']\n', end="")
    print(f"Size of the queue: {queue._size}")

    while queue._size > 0:
        print(f"Element deleted: {queue.dequeue()} - Size: {queue._size}")
