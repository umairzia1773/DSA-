class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            last_node = self.head.prev
            new_node.next = self.head
            new_node.prev = last_node
            self.head.prev = new_node
            last_node.next = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            last_node = self.head.prev
            new_node.next = self.head
            new_node.prev = last_node
            self.head.prev = new_node
            last_node.next = new_node

    def insert_after(self, key, data):
        new_node = Node(data)
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp:
            if temp.data == key:
                next_node = temp.next
                temp.next = new_node
                new_node.prev = temp
                new_node.next = next_node
                next_node.prev = new_node
                if temp == self.head.prev:
                    self.head.prev = new_node
                break
            temp = temp.next
            if temp == self.head:
                print("Key not found in the list")
                break

    def insert_sorted(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return
        temp = self.head
        while temp.data < data and temp.next != self.head:
            temp = temp.next
        if temp == self.head:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node
        elif temp.data >= data:
            new_node.next = temp
            new_node.prev = temp.prev
            temp.prev.next = new_node
            temp.prev = new_node
        else:  # insert at end
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node

    def delete(self, key):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                last_node = self.head.prev
                second_node = self.head.next
                last_node.next = second_node
                second_node.prev = last_node
                self.head = second_node
            return
        temp = self.head.next
        while temp != self.head:
            if temp.data == key:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            temp = temp.next
        print("Key not found in the list")

    def search(self, key):
        if not self.head:
            print("List is empty")
            return False
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=' <-> ')
            temp = temp.next
            if temp == self.head:
                break
        print()


if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()
    cdll.insert_sorted(5)
    cdll.insert_sorted(10)
    cdll.insert_sorted(7)
    cdll.insert_sorted(3)
    print("Circular Doubly Linked List:")
    print("============================")
    cdll.display()
    print("----------------------------")

    cdll.insert_sorted(80)
    print("List after insertion of 80:")
    print("==============================")
    cdll.display()
    print("------------------------------")
    cdll.delete(7)
    print("List after deletion of 7:")
    print("============================")
    cdll.display()
    print("----------------------------")
    print()
    print("------------------------------")
    print("Is 7 present in the list?", cdll.search(7))
    print("Is 15 present in the list?", cdll.search(15))
    print("--------------------------------")


