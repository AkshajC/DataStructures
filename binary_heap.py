class Minheap:
    def __init__(self):
        self.binary_heap = []

    def heapify(self):
        try:
            for i in range(len(self.binary_heap)):
                if self.binary_heap[i] > self.binary_heap[2 * i + 1]:
                    self.binary_heap[i], self.binary_heap[2 * i + 1] = self.binary_heap[2 * i + 1], self.binary_heap[i]
                if self.binary_heap[i] > self.binary_heap[2 * i + 2]:
                    self.binary_heap[i], self.binary_heap[2 * i + 2] = self.binary_heap[2 * i + 2], self.binary_heap[i]
        except IndexError:
            pass

    def add(self, new_item):
        self.binary_heap.append(new_item)
        self.heapify()

    def remove(self, index):
        self.binary_heap[index], self.binary_heap[len(self.binary_heap) - 1] = self.binary_heap[len(self.binary_heap) - 1], self.binary_heap[index]
        self.binary_heap.pop()
        self.heapify()

    def peek(self):
        return self.binary_heap[0]

    def extract_min(self):
        return self.binary_heap.pop()

    def display(self):
        print(self.binary_heap)


def test():
    h = Minheap()
    h.binary_heap = [4, 1, 2, 71, 24, 11]
    h.heapify()
    h.display()
    h.remove(1)
    h.display()
    h.add(100)
    h.display()


if __name__ == '__main__':
    test()
