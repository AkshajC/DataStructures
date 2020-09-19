class Minpriority:

    def __init__(self, heap):
        self.heap = heap

    def min_bubble_heapify(self):
        x = 0
        for i in range(0, len(self.heap)):
            try:
                if self.heap[2 * i + 1] <= self.heap[i]:
                    self.heap[2 * i + 1], self.heap[i] = self.heap[i], self.heap[2 * i + 1]
                    x += 1
                if self.heap[2 * i + 2] <= self.heap[i]:
                    self.heap[2 * i + 2], self.heap[i] = self.heap[i], self.heap[2 * i + 2]
                    x += 1
            except:
                pass
        if x > 0:
            return True
        else:
            return False

    def heapify(self):
        is_heap = True
        while is_heap:
            is_heap = self.min_bubble_heapify()

    def add(self, element):
        self.heap.append(element)
        self.heapify()

    def display(self):
        print(self.heap)

    def poll(self):
        self.heap.pop(0)

    def peek(self):
        print(self.heap[0])

class Maxpriority:

    def __init__(self, heap):
        self.heap = heap

    def max_bubble_heapify(self):
        x = 0
        for i in range(0, len(self.heap)):
            try:
                if self.heap[2 * i + 1] >= self.heap[i]:
                    self.heap[2 * i + 1], self.heap[i] = self.heap[i], self.heap[2 * i + 1]
                    x += 1
                if self.heap[2 * i + 2] >= self.heap[i]:
                    self.heap[2 * i + 2], self.heap[i] = self.heap[i], self.heap[2 * i + 2]
                    x += 1
            except:
                pass
        if x > 0:
            return True
        else:
            return False

    def heapify(self):
        is_heap = True
        while is_heap:
            is_heap = self.max_bubble_heapify()

    def add(self, element):
        self.heap.append(element)
        self.heapify()

    def display(self):
        print(self.heap)

    def poll(self):
        self.heap.pop(0)

    def peek(self):
        print(self.heap[0])

