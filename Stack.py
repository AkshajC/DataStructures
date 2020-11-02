class Stack:
    def __init__(self, stack_limit):
        self.stack_limit = stack_limit
        self.stack = []

    def is_full(self):
        if len(self.stack) == self.stack_limit:
            return True
        else:
            return False

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, new_item):
        if self.is_full():
            print("This stack is full")
        else:
            self.stack.append(new_item)

    def pop(self):
        if self.is_empty():
            print("This stack is empty")
        else:
            self.stack.pop()

    def peek(self):
        return self.stack[-1]

if __name__ == "__main__":
    our_stack = Stack(5)
    our_stack.pop()
    our_stack.push(1)
    print(our_stack.stack)
    our_stack.push(2)
    print(our_stack.stack)
    our_stack.push(3)
    print(our_stack.stack)
    our_stack.push(4)
    print(our_stack.stack)
    our_stack.push(5)
    print(our_stack.stack)
    our_stack.push(6)
    print(our_stack.stack)
    our_stack.peek()
    our_stack.pop()
    print(our_stack.stack)
    our_stack.pop()
    print(our_stack.stack)
    our_stack.pop()
    print(our_stack.stack)
    our_stack.pop()
    print(our_stack.stack)
    our_stack.pop()
    print(our_stack.stack)
    our_stack.pop()
    print(our_stack.stack)




