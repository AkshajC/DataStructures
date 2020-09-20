from double_linked_list import Node, DoubleLinkedList


class HashTable:

    def __init__(self):
        self.hash_table = [None for i in range(30)]
        self.key_store = [[] for i in range(30)]

    def hash(self, item):
        item = str(item)
        hash_value = 0
        for element in item:
            hash_value += ord(element)
        return hash_value % 10

    def chain(self, key, val, position):
        dl = DoubleLinkedList()
        dl.head = Node([self.key_store[position], self.hash_table[position]])
        dl.add([key, val], len(dl.linked_gen()) + 1)
        self.hash_table[position] = dl

    def display(self, show_none=False):
        x = 0
        if not show_none:
            filtered_list = []
            for element in self.hash_table:
                x += 1
                if element is not None:
                    if isinstance(element, DoubleLinkedList):
                        for link in element.linked_gen():
                            filtered_list.append(link)

                    else:
                        filtered_list.insert(x, element)
            print(filtered_list)
        else:
            filtered_list = []
            for element in self.hash_table:
                x += 1
                if isinstance(element, DoubleLinkedList):
                    for link in element.linked_gen():
                        filtered_list.append(link)

                else:
                    filtered_list.insert(x, element)

            print(filtered_list)

    def add(self, key, val):
        hash_value = self.hash(key)
        if self.hash_table[hash_value] is None:
            self.key_store[hash_value] = key
            self.hash_table.insert(hash_value, val)
        else:
            self.chain(key, val, hash_value)

    def ind_remove(self, index, chained_index=None):
        item = self.hash_table[index]
        if isinstance(item, DoubleLinkedList):
            item.remove(chained_index + 1)

        elif item is None:
            print("That index is a None type")
            pass

        else:
            self.hash_table.remove(self.hash_table[index])

    def value(self, index, chained_index=None):
        item = self.hash_table[index]
        if isinstance(item, DoubleLinkedList):
            linked_item = item.linked_gen()
            if len(linked_item) > 1:
                linked_item = item.linked_gen()[chained_index + 1]
            else:
                linked_item = item.linked_gen()[0]
            print(linked_item)

        elif item is None:
            print("That index is a None type")
            pass

        else:
            self.hash_table.remove(self.hash_table[index])

if __name__ == '__main__':
    hash_ = HashTable()
    hash_.add("Name", "Akshaj")
    hash_.display()
    hash_.add("Name", "Akshaj")
    hash_.display()
    hash_.display()
    hash_.add("mood", "happy")
    hash_.display()
    hash_.display(show_none=True)
    hash_.ind_remove(1)
    hash_.display()
    hash_.ind_remove(0)
    hash_.ind_remove(5, 1)
    hash_.display()
    hash_.display(show_none=True)
    hash_.value(5, 1)


