class CircleQueue:

    def __init__(self, queue_limit, linear_queue_limit):
        self.queue = []
        self.queue_limit = queue_limit
        self.front = -1
        self.rear = -1
        self.linear_queue_limit = linear_queue_limit

    def is_full(self):
        if len(self.queue) == self.queue_limit:
            return True
        else:
            return False

    def is_empty(self):
        if len(self.queue) == 0:
            self.rear = -1
            self.front = -1
            return True
        else:
            return False

    def enqueue(self, new_item):
        if self.is_full():
            print("The circle queue is full")
        elif self.rear + 1 < self.linear_queue_limit:
            self.queue.append(new_item)
            self.rear += 1
            if len(self.queue) == 1:
                self.front = 0
        else:
            self.queue.insert((self.rear + 1) % self.linear_queue_limit, new_item)
            self.rear += 1
            if len(self.queue) == 1:
                self.front = 0

    def dequeue(self):
        if self.is_empty():
            print("The circular queue is empty")
            self.front = -1
            self.rear = -1
        elif len(self.queue) == 1:
            self.queue.pop()
            self.front += 1
        elif self.rear + 1 > self.linear_queue_limit:
            self.queue.pop((self.rear + 1) % self.linear_queue_limit - 1)
            self.front += 1
        else:
            self.queue.pop((self.rear + 1) % self.linear_queue_limit)
            self.front += 1

    def display(self):
        print(self.queue)


def main():
    q = CircleQueue(7, 5)
    q.enqueue(1)
    q.display()
    q.enqueue(2)
    q.display()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.display()
    q.dequeue()
    q.dequeue()
    q.display()
    q.enqueue(6)
    q.enqueue(7)
    q.display()
    q.dequeue()
    q.dequeue()
    q.display()
    q.dequeue()
    q.display()
    q.dequeue()
    q.display()
    q.dequeue()
    q.display()
    q.display()


if __name__ == '__main__':
    main()
