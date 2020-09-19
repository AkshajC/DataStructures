class Node:

    def __init__(self, item):
        self.next = None
        self.prev = None
        self.item = item


class DoubleCircularLinkedList:

    def __init__(self, linked=[]):
        self.linked = linked
        self.hiddenlink = linked
        self.head = Node(None)

    def init_setup(self):
        x = 0
        for item in self.hiddenlink:
            x += 1
            cur_node = Node(item)
            if x == 1:
                self.head = cur_node
            prev_node = cur_node
            cur_node = cur_node.next
            prev_node.next = cur_node


    def hidden_update(self, item):
        self.hiddenlink.append(item)

    def display(self):
        cur_node = self.head
        display_list = []
        x = 0
        while cur_node is not None and x < len(self.hiddenlink):
            display_list.append(cur_node.item)
            cur_node = cur_node.next
            x += 1
        print(display_list)

    def add(self, item, index):
        if index == 0:
            cur_node = self.head
            x = 0
            while cur_node is not None and x < len(self.hiddenlink):
                cur_node = cur_node.next
                x += 1
            if self.head.item is not None:
                new_node = Node(item)
                new_node.next = self.head
                self.head = new_node
                self.head.prev = cur_node
                self.hidden_update(item)
                cur_node.next = self.head
            else:

                self.head = Node(item)
                self.hidden_update(item)

        elif 0 < index < len(self.hiddenlink):
            x = 0
            cur_node = self.head
            while cur_node.next is not None and x < index:
                if x + 1 == index:
                    prev_node = cur_node
                print(cur_node.item)
                cur_node = cur_node.next
                x += 1
            new_node = Node(item)
            prev_node.next = new_node
            new_node.next = cur_node
            print(prev_node.item)
            print(new_node.item)
            self.hidden_update(item)
            cur_node.next = self.head

        else:
            cur_node = self.head
            x = 0
            while cur_node.next is not None and x < len(self.hiddenlink):
                cur_node = cur_node.next
            new_node = Node(item)
            cur_node.next = new_node
            new_node.next = self.head

    def remove(self, index):
        cur_node = self.head
        x = 0
        if index > len(self.hiddenlink):
            return None
        if index == 0:
            next_node = cur_node.next
            del cur_node
            self.head = next_node
        elif len(self.hiddenlink) - 1 > index > 0:
            while cur_node is not None and x < index:
                if x + 1 == index:
                    prev_node = cur_node
                cur_node = cur_node.next
                x += 1
            next_node = cur_node.next
            prev_node.next = next_node
            del cur_node
        else:
            while cur_node is not None and x < len(self.hiddenlink):
                if x + 1 == len(self.hiddenlink):
                    prev_node = cur_node
                cur_node = cur_node.next
                x += 1
            del cur_node
            prev_node.next = self.head


def main():
    d = DoubleCircularLinkedList()
    d.add(2, 0)
    print(d.head.item)
    d.display()
    d.add(3, 0)
    print(d.head.next.item)
    d.display()
    print(d.head.item)
    d.add(1, 0)
    d.display()
    print(d.head.next.next.item)
    d.add(2, 1)
    d.display()
    print(d.head.item)
    print(d.head.next.item)
    print(d.head.next.next.item)
    print(d.head.next.next.next.item)
    print(d.head.next.next.next.next.item)
    print(d.head.item)


if __name__ == '__main__':
    main()





