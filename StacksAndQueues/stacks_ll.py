class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self._size = 0

    def push(self, data):
        # Create a new node
        newNode = Node(data)
        if self.top:
            newNode.next = self.top
            self.top = newNode
        else:
            self.top = newNode
        self._size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self._size -= 1
            if self.top.next: # check if there is more than one node.
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            print("Stack is empty!")

    def peek(self):
        if self.top:
            return self.top.data
        else:
            print("Stack is empty!")

    def __repr__(self) -> str:
        repr = "Stack: ["
        current = self.top
        if current:
            while (current):
                if current.next:
                    repr += f"{current.data} -> "
                else:
                    repr += f"{current.data}]"
                current = current.next
        else:
            repr += "]"
        return repr

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack)
    print(f"Top: {stack.peek()}")

    print(f"First delete: {stack.pop()}")
    print(stack)
    print(f"Top: {stack.peek()}")



