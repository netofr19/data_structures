# Implementation of stacks using array

size = 3
data = [0] * size  # Initialize the stack
top = -1

def push(x):
    global top
    if top>=size-1:
        print("Stack Overflow!")
    else:
        top = top + 1
        data[top] = x

def pop():
    global top
    if top == -1:
        print('Stack Underflow!')
    else:
        aux = data[top]
        top = top - 1
        return aux

def peek():
    global top
    if top == -1:
        print("Stack is empty!")
    else:
        return (data[top])

if __name__ == '__main__':
    push(10)
    push(20)
    push(30)

    print(data[0:top+1])

    push(40)
    push(50)

    print(pop())
    print(f"Peek={peek()}")
    print(pop())
    print(f"Peek={peek()}")

    print(data[0:top + 1])
    print(f"Peek={peek()}")