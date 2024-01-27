class Node:
    def __init__(self, data):
        if data is not None:
            self._data = data
        else:
            raise ValueError("Data cannot be None for the Node")
        self.next = None

    def set_data(self, new_data):
        if new_data is not None:
            self._data = new_data
        else:
            raise ValueError("Data cannot be None for the Node")

    def get_data(self):
        return self._data


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.get_data(), end=" -> ")
            current = current.next
        print("None")

    def add_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_node_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add_node_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            position = 0
            while position < index - 1 and current:
                current = current.next
                position += 1
            if current is None:
                print("Index out of range")
                return
            new_node.next = current.next
            current.next = new_node


    def add_sorted(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        if data < self.head.get_data():
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head

        while current.next and data > current.next.get_data():
            current = current.next
        new_node.next = current.next
        current.next = new_node


    def remove_first_node(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            temp = None

    def remove_last_node(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None


    def remove_node_by_value(self, data):
        current = self.head
        if current and current.get_data() == data:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.get_data() != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None


    def remove_node_by_index(self, index):
        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp = None
            return

        current = self.head
        position = 0
        while current and position < index:
            prev = current
            current = current.next
            position += 1

        if current is None:
            return
        prev.next = current.next
        current = None


    def search_by_value(self, data):
        current = self.head
        index = 0
        while current:
            if current.get_data() == data:
                return f"{data} Found at index {index}"
            current = current.next
            index += 1
        return "Not found"


if __name__ == "__main__":
    LL = LinkedList()
    LL.add_node(5)
    LL.add_node(10)
    LL.add_node(15)
    LL.add_node(20)
    LL.add_node_at_beginning(2)
    LL.add_node_at_end(30)
    LL.add_node_at_index(17,2)
    LL.add_sorted(8)
    print("Original list:")
    print("==============")
    LL.print_list()
    print()
    print(LL.search_by_value(17))
    LL.remove_first_node()
    LL.remove_last_node()
    LL.remove_node_by_value(10)

    print("\nAfter Removing Nodes")
    print("=====================")
    LL.print_list()
