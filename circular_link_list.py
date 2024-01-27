class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert_sorted(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        elif self.head.data >= new_node.data:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, value):
        if not self.head:
            print("Circular Linked List is empty")
            return

        if self.head.data == value:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            return

        prev = None
        curr = self.head
        while curr.next != self.head:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        if curr.data == value:
            prev.next = self.head

    def search(self, value):
        if not self.head:
            print("Circular Linked List is empty")
            return False

        temp = self.head
        while True:
            if temp.data == value:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def display(self):
        if not self.head:
            print("Circular Linked List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print()


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_sorted(5)
    cll.insert_sorted(10)
    cll.insert_sorted(7)
    cll.insert_sorted(3)
    print("Circular Linked List:")
    print("=====================")
    cll.display()
    print("---------------------")
    cll.insert_sorted(8)
    print("Circular Linked List after insertion of 8:")
    print("==========================================")
    cll.display()
    print("----------------------------------------")

    cll.delete(7)
    print("Circular Linked List after deletion of 7:")
    print("=========================================")
    cll.display()
    print()
    print("------------------------------------------")
    print("Is 10 present in the list?", cll.search(10))
    print("Is 100 present in the list?", cll.search(100))
    print("------------------------------------------")
