class Queue:
    def __init__(self, queue_limit):
        self.queue_limit = queue_limit
        self.queue = []
        self.front = -1
        self.rear = -1

    def is_empty(self):
        if self.queue:
            return False
        else:
            return True

    def is_full(self):
        if len(self.queue) == self.queue_limit:
            return True
        else:
            return False

    def enqueue(self, new_item):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue.append(new_item)
            self.rear += 1
            if len(self.queue) == 1:
                self.front = 0
            print(self.rear)
            print(self.front)


    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.queue.pop(0)
            if self.is_empty():
                self.rear = -1
                self.front = -1
            else:
                self.front += 1
            print(self.rear)
            print(self.front)



    def display(self):
        print(self.queue)

    def peek(self):
        if self.is_empty():
            print("This queue is empty")
        else:
            return self.queue[0]





if __name__ == "__main__":
    x = Queue(5)
    print(x.rear)
    print(x.front)
    x.enqueue(1)
    x.display()
    x.enqueue(2)
    x.display()
    x.enqueue(3)
    x.display()
    x.enqueue(4)
    x.display()
    x.enqueue(5)
    x.display()
    x.enqueue(6)
    x.display()
    x.dequeue()
    x.display()
    x.dequeue()
    x.display()
    x.dequeue()
    x.display()
    x.dequeue()
    x.display()
    x.dequeue()
    x.display()
    x.dequeue()
    x.display()

