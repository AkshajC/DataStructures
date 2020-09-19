import sys


class Node:
    def __init__(self, item):
        self.next = None
        self.item = item


class LinkedList:

    def __init__(self):
        self.head = Node(None)

    def is_empty(self):
        if len(self.linked_gen()) == 0:
            return True
        else:
            return False

    def display(self):
        global linked_list
        linked_list = []
        current_node = self.head
        while current_node.next is not None:
            linked_list.append(current_node.item)
            current_node = current_node.next
        linked_list.append(current_node.item)
        print(linked_list)

    def linked_gen(self):
        linked_list = []
        current_node = self.head
        while current_node.next is not None:
            linked_list.append(current_node.item)
            current_node = current_node.next
        linked_list.append(current_node.item)
        return linked_list

    def add(self, new_item, position=1):
        current_node = self.head
        if position == 1:
            ahead_node = self.head.next
            new_node = Node(self.head.item)
            self.head.item = new_item
            self.head.next = new_node
            new_node.next = ahead_node

        elif position > 1 and position < len(self.linked_gen()) + 1:
            for node in range(1, position - 1):
                current_node = current_node.next
            next_node = current_node.next
            new_node = Node(new_item)
            current_node.next = new_node
            new_node.next = next_node

        else:
            try:
                for node in range(1, position - 1):
                    current_node = current_node.next
                new_node = Node(new_item)
                current_node.next = new_node
            except  :
                print("That position is out of range")

    def remove(self, position):
        if position == 1:
            del_node = self.head.next
            next_node = del_node.next
            self.head.item = del_node.item
            self.head.next = next_node
            del del_node

        else:
            current_node = self.head
            for node in range(1, position - 1):
                current_node = current_node.next
            del_node = current_node.next
            next_node = del_node.next
            current_node.next = next_node
            del del_node

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def find_even_or_odd(self, even=True):
        current_node = self.head
        perfect_nodes = []
        x = 0
        if even:
            while current_node:
                x += 1
                if x % 2 == 0:
                    perfect_nodes.append(current_node.item)
                current_node = current_node.next
        else:
            while current_node:
                x += 1
                if x % 2 == 1:
                    perfect_nodes.append(current_node.item)
                current_node = current_node.next

        print(perfect_nodes)

    def is_k_large(self, k):
        length = len(self.linked_gen())
        if k >= length and k != 1:
            print("The k value too large")
            k = input("Give me a new value for k: ")
        if k >= length and k != 1:
            self.is_k_large(k)
        else:
            return k

    def kth_element(self, k, reverse=False):
        current_node = self.head
        x = 0
        if self.head.item == None:
            print("Linked list is empty")
            sys.exit()
        k = self.is_k_large(k)
        if len(self.linked_gen()) == 1:
            return self.head.item
        else:
            if reverse:
                k_behind_node = self.head
                while current_node:
                    if x >= k:
                        k_behind_node = k_behind_node.next
                    x += 1
                    current_node = current_node.next
                return k_behind_node.item
            else:
                while k:
                    k -= 1
                    if k == 0:
                        break
                    current_node = current_node.next
                return current_node.item



LinkedList = LinkedList()
LinkedList.head.item = "w"
LinkedList.find_even_or_odd(even=True)
LinkedList.find_even_or_odd(even=False)
print(LinkedList.kth_element(1, reverse=True))
print(LinkedList.kth_element(1, reverse=False))
LinkedList.add("hi",2)
LinkedList.display()
