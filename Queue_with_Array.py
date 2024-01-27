class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size
        self.front = self.rear = -1

class Queue:
    def __init__(self, size):
        self.array = Array(size)

    def is_full(self):
        return (self.array.rear + 1) % self.array.size == self.array.front

    def is_empty(self):
        return self.array.front == -1

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full, Increase the Capacity to Add elements.")
            return
        elif self.is_empty():
            self.array.front = self.array.rear = 0
        else:
            self.array.rear = (self.array.rear + 1) % self.array.size
        self.array.array[self.array.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty, Enqueue some elements first")
            return None
        data = self.array.array[self.array.front]
        if self.array.front == self.array.rear:
            self.array.front = self.array.rear = -1
        else:
            self.array.front = (self.array.front + 1) % self.array.size
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is Empty.")
            return None
        return self.array.array[self.array.front]

    def display(self):
        if self.is_empty():
            print("Queue is Empty.")
            return
        print("QUEUE:", end=" ")
        i = self.array.front
        while i != self.array.rear:
            print(self.array.array[i], end=" ")
            i = (i + 1) % self.array.size
        print(self.array.array[self.array.rear])


if __name__ == "__main__":
    queue = Queue(5)
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
