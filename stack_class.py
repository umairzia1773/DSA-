class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.prev = new_node
            new_node.next = new_node
            self.top = new_node
        else:
            new_node.next = self.top
            new_node.prev = self.top.prev
            self.top.prev.next = new_node
            self.top.prev = new_node
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        data = self.top.data
        if self.size == 1:
            self.top = None
        else:
            self.top.prev.next = self.top.next
            self.top.next.prev = self.top.prev
            self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data

    def search(self, value):
        if self.is_empty():
            return -1
        index = 0
        current = self.top
        while True:
            if current.data == value:
                return index
            current = current.next
            index += 1
            if current == self.top:
                break
        return -1

    def clear(self):
        self.top = None
        self.size = 0

    def display(self):
        if self.is_empty():
            print("\tStack is Empty")
            return
        current = self.top
        print("Top -->", end=" ")
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.top:
                break
        print("<-- Bottom")


if __name__ == "__main__":
    stack = Stack()
    stack.push(18)
    stack.push(22)
    stack.push(35)
    stack.push(45)
    stack.push(98)

    print("Stack:")
    print("======")
    stack.display()

    print("\nPeek:", stack.peek())
    print("=====")

    print("Size:", stack.get_size())
    print("=====")

    print("Searched element in Stack is at position:", stack.search(35))

    stack.pop()
    print("\nStack after pop:")
    print("================")
    stack.display()
    stack.clear()
    print()
    print("--------------------")
    print("Stack after Clearing:")
    stack.display()
    print("--------------------")
