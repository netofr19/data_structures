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

    def search(self, data):
        current = self.head
        if current.data == data:
            return True
        else:
            current = current.next
            while current != self.head:
                if current.data == data:
                    return True
                current = current.next
        return False

    def delete(self, data):
        current = self.head
        prev = self.head
        while current.data != data and prev != self.tail:
            prev = current
            current = current.next
        if current.data == data:
            if current == self.head:
                self.tail.next = current.next
                self.head = current.next
            elif current == self.tail:
                prev.next = self.head
                self.tail = prev
            else:
                # item to be deleted is an intermediate node
                prev.next = current.next
            self._size -= 1
            return current.data
        else:
            print("The item is not in the list")
            return None

if __name__ == '__main__':
    words = CircularList()

    words.append('eggs')
    words.append('ham')
    words.append('spam')

    words.display()

    print(f"'spam' exists on the list: {words.search('spam')}")
    print(f"'bacon' exists on the list: {words.search('bacon')}")

    print(f"Delete on the list: {words.delete('ham')}")
    print(f"Delete on the list: {words.delete('bacon')}")
