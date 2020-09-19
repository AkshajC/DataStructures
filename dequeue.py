class Dequeue:

    def __init__(self, limit):
        self.limit = limit
        self.dequeue = []

    def is_full(self):
        if len(self.dequeue) == self.limit:
            return True
        else:
            return False

    def is_empty(self):
        if len(self.dequeue) == 0:
            return True

        else:
            return False

    def appendleft(self, new_item):
        if self.is_full():
            print("The dequeue is full")

        else:
            self.dequeue.insert(0, new_item)

    def appendright(self, new_item):
        if self.is_full():
            print("The dequeue is full")

        else:
            self.dequeue.append(new_item)

    def removeleft(self):
        if self.is_empty():
            print("the dequeue is empty")
        else:
            self.dequeue.pop(0)

    def removeright(self):
        if self.is_empty():
            print("the dequeue is empty")
        else:
            self.dequeue.pop()

    def display(self):
        print(self.dequeue)
