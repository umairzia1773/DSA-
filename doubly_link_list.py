class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def addSorted(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif data <= self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif data >= self.tail.data:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def add_at_Position(self, data, position):
        if position <= 0:
            self.insert_at_head(data)
        else:
            new_node = Node(data)
            current = self.head
            count = 0
            while count < position - 1 and current.next:
                current = current.next
                count += 1
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def Delete_from_Head(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def Delete_from_Tail(self):
        if self.tail:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def DeleteObject(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.deleteHead()
                elif current == self.tail:
                    self.deleteTail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                break
            current = current.next

    def SearchObject(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display_forward(self):
        if not self.head:
            print("Doubly Linked List is Empty")
            return

        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print()

    def display_backward(self):
        if not self.tail:
            print("Doubly Linked List is Empty")
            return

        current = self.tail
        while current:
            print(current.data, end=' <-> ')
            current = current.prev
        print()

if __name__ == "__main__":

    dll = DoublyLinkedList()
    dll.insert_at_head(10)
    dll.insert_at_tail(20)
    dll.insert_at_head(30)
    dll.insert_at_tail(40)
    dll.addSorted(15)
    dll.add_at_Position(17, 1)

    print("Doubly Linked List (Forward Printing):")
    dll.display_forward()

    print("\nDoubly Linked List (Backward Printing):")
    dll.display_backward()
    print()
    print("Doubly Link List after Deleting:")
    print("===============================")
    dll.Delete_from_Head()
    dll.Delete_from_Tail()
    dll.DeleteObject(30)
    print("Forward printing:")
    print("----------------")
    dll.display_forward()
    print("Backward printing:")
    print("-----------------")
    dll.display_backward()
    print()
    print("Is 10 present in the Doubly Link List?", dll.SearchObject(10))
