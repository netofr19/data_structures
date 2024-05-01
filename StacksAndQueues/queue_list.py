class ListQueue:
    def __init__(self):
        self.items = []
        self.front = self.rear = 0
        self.size = 5 # Maximum capacity of the queue

    def enqueue(self, data):
        if self.size == self.rear:
            print("aQueue is full!")
        else:
            self.items.append(data)
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty!")
        else:
            data = self.items.pop(0) # delete the item from front
            self.rear -= 1
            return data


if __name__ == '__main__':
    q = ListQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)

    print(q.items)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.dequeue()

    print(q.items)