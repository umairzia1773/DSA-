class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return False
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = item
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.max_size
            return item

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.max_size - self.front + self.rear + 1

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        print("Front -->", end=" ")
        while True:
            print(self.queue[temp], end=" ")
            if temp == self.rear:
                break
            temp = (temp + 1) % self.max_size
        print("<-- Rear")

if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)

    print("Circular Queue:")
    print("===============")
    cq.display()

    print("\nDequeuing:", cq.dequeue())
    print("==========")

    print("\nPeek at Front element:", cq.peek())
    print("======================")

    print("\nIs Queue full?", cq.is_full())
    print("==============")
