class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("QUEUE:", end=" ")
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(23)
    queue.enqueue(39)
    queue.enqueue(17)
    queue.display()
    print("==================")
    print("Peeked Value:", queue.peek())
    print("------------------")
    print("Dequeued value from Queue:", queue.dequeue())
    print("-----------------------------")
    queue.display()
