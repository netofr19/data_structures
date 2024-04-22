class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        self._size += 1

    def display(self):
        current = self.head
        print(current.data)
        current = current.next
        while current != self.head:
            print(current.data)
            current = current.next

if __name__ == '__main__':
    words = CircularList()

    words.append('eggs')
    words.append('ham')
    words.append('spam')

    words.display()