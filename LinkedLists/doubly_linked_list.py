class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def append(self, data):
        """
        Append an item at the end of the list.
        """
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self._size += 1

    def insert(self, data, index):
        newNode = Node(data)
        if index==0:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            self._size += 1
        elif index == self.size():
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self._size += 1
        elif index >0 and index <self.size():
            ...
        else:
            print("====== Out of Range ========")


if __name__ == '__main__':
    words = DoublyLinkedList()
    words.insert('egg', 0)
    words.insert('ham', 0)
    words.insert('spam', 0)

    print("Items in doubly linked list after insert: ")
    current = words.head
    while current:
        print(current.data)
        current = current.next
            