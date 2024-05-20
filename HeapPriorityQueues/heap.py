class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    def arrange(self, k):
        while k//2>0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    def minchild(self, k):
        if k * 2 +1 > self.size:
            return k * 2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2 + 1
        
    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.minchild(k)
            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def delete_at_root(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item
    
    def delete_at_location(self, location):
        item = self.heap[location]
        self.heap[location] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(location)
        return item
    
    def heap_sort(self):
        sorted_list = []
        for node in range(self.size):
            n = self.delete_at_root()
            sorted_list.append(n)

        return sorted_list

if __name__ == '__main__':
    h = MinHeap()

    unsorted_list = [4,8,7,2,9,10,5,1,3,6]

    for i in unsorted_list:
        h.insert(i)

    print(f"Unsorted list: {unsorted_list}")

    sorted_list = h.heap_sort()

    print(f"Sorted list: {sorted_list}")