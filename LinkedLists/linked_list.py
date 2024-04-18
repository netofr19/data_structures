class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, data):
        newNode = Node(data)

        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
            self._size += 1
        else:
            self.head = newNode
            self.tail = self.head
            self._size += 1

    def insert(self, data, index):
        newNode = Node(data)

        current = self.head
        prev = current
        count = 0

        while current:
            if index == 0:
                newNode.next = current
                self.head = newNode
                self._size += 1
                return
            elif index == count:
                newNode.next = current
                prev.next = newNode
                self._size += 1
                return
            elif current.next == None and index == count+1:
                current.next = newNode
                self._size += 1
                return
                        
            count += 1
            prev = current
            current = current.next

        if count < index:
            print("The list has less number of elements!")

    def search(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def size(self):
        return self._size
    
    def delete(self, index):
        if index == 0:
            current = self.head
            if self.head is None:
                print("No data element to delete!")
            else:
                self.head = current.next
                self._size -= 1
        elif index==self.size()-1:
            current = self.head
            prev = current
            while current.next:
                prev = current
                current = current.next
            prev.next = current.next
            self._size -= 1
            print(f"Index {index} deleted successfully")
        elif index > self.size()-1:
            print('----- Out of range! ------')
        else:
            current = self.head
            prev = current
            for _ in range(0, index, 1):
                prev = current
                current = current.next
            prev.next = current.next
            self._size -= 1
            print(f"Index {index} deleted successfully")

    def remove(self, data):
        current = self.head
        prev = current
        while current != None and current.data != data:
            prev = current
            current = current.next
        if current == self.head:
            self.head = current.next
            self._size -= 1
            print(f"Value {data} deleted successfully")
        elif current != None:
            prev.next = current.next
            self._size -= 1
            print(f"Value {data} deleted successfully")
        else:
            print("The value is not on the list!")

    def clear(self):
        # clear the entire list
        self.head = None
        self.tail = None
        self._size = 0

    def display(self):
        current = self.head
        print("Linked List:")
        while current:
            if current.next:
                print(current.data, end="-> ")
            else:
                print(current.data, end=" ")
            current = current.next
        print('')

if __name__ == "__main__":
    
    print('\n----------- LINKED LIST -------------\n')

    opt = None
    ll = None

    while True:

        print('------------------------------------------')
        print('COMMAND OPTIONS:')
        print('[1]- Create a Linked List')
        print('[2]- Append an element')
        print('[3]- Insert an element in a specific position')
        print('[4]- Search for a specific element')
        print('[5]- See the length of the list')
        print('[6]- Delete an element by position')
        print('[7]- Remove an element by value')
        print('[8]- Clear the Linked List')
        print('[9]- Print the Linked List')
        print('[10]- Exit')
        print('------------------------------------------')

        opt = int(input('Choose an option: '))
        print('')

        if opt == 1:
            ll = SinglyLinkedList()
            print("Linked List created!\n")
        elif opt == 2:
            value = int(input('Enter the value: '))
            ll.append(value)
            print(f"{value} successfully added!\n")
        elif opt == 3:
            value = int(input("Enter the value: "))
            index = int(input("Enter the index: "))
            ll.insert(value, index)
            print(f"{value} successfully added at index {index}!")
        elif opt == 4:
            value = int(input('Enter the value to be sought: '))
            isPresent = ll.search(value)
            print(f"The value {value} is present in the list: {isPresent}")
        elif opt == 5:
            if ll:
                print(f"The current length of the list is: {ll.size()}")
            else:
                print("The list does not exist yet!\n")
        elif opt == 6:
            index = int(input("Inform the index to be deleted: "))
            ll.delete(index)
        elif opt == 7:
            value = int(input("Inform the value to be deleted: "))
            ll.remove(value)
        elif opt == 8:
            ll.clear()
        elif opt == 9:
            if isinstance(ll, SinglyLinkedList):
                if ll.size() > 0:
                    ll.display()
                else:
                    print("The list is empty!")
            else:
                print("The list does not exist yet!\n")
        elif opt == 10:
            print("See you next time!")
            break
        else:
            print('Invalid option, please choose again!')

