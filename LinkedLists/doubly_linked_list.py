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
            current = self.head
            prev = self.head
            for _ in range(index):
                prev = current
                current = current.next
            newNode.prev = prev
            newNode.next = current
            prev.next = newNode
            current.prev = newNode
            self._size += 1
        else:
            print("====== Out of Range ========")

    def search(self, data):
        current = self.head
        pos = 0
        while current:
            if current.data == data:
                print(f"Data item is present in the list at index {pos}")
                return None
            current = current.next
            pos += 1
        print("Data item is not present in the list")
        return None

    def delete(self, index):
        # Delete a node from the list
        current = self.head
        if current is None:
            print("The list is empty")
            return None

        if index == 0:
            self.head = current.next
            return current.data
        elif index > 0 and index < self.size()-1:
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            return current.data
        elif index == self.size()-1:
            for _ in range(self.size()-1):
                current = current.next
            current.prev.next = None
            self.tail = current
            return current.data
        else:
            print('====== Out of Range ========')
            return None




if __name__ == '__main__':
    words = DoublyLinkedList()
    words.insert('egg', 0)
    words.insert('ham', 0)
    words.insert('spam', 0)

    print("Items in doubly linked list before insert: ")
    current = words.head
    while current:
        print(current.data)
        current = current.next

    words.insert('bacon', 1)
    words.insert('bread', 2)

    print("\nItems in doubly linked list after insert: ")
    current = words.head
    while current:
        print(current.data)
        current = current.next

    print('')

    words.search('fruit')

    print('')

    print(words.delete(3))


    print("\nItems in doubly linked list after delete: ")
    current = words.head
    while current:
        print(current.data)
        current = current.next

            