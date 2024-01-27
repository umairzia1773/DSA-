class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return i // 2

    def left_child(self, i):
        return 2 * i

    def right_child(self, i):
        return 2 * i + 1

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        max_index = i
        left = self.left_child(i)
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        right = self.right_child(i)
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
        if i != max_index:
            self.swap(i, max_index)
            self.heapify_down(max_index)

    def add(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if not self.heap:
            return None
        max_element = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return max_element

    def print_heap(self):
        print("MAX HEAP:", self.heap)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def heap_sort(self):
        sorted_heap = []
        while self.heap:
            max_element = self.delete_max()
            sorted_heap.append(max_element)
        return sorted_heap


def main():
    MH = MaxHeap()
    elements = [22, 74, 56, 31, 100, 171, 46, 88]

    for ele in elements:
        MH.add(ele)

    print("ORIGNAL MAX-HEAP:")
    print("=================")
    MH.print_heap()
    print("=========")

    max_element = MH.delete_max()
    print("\nDELETED MAXIMUM ELEMENT:", max_element)
    print("========================")
    print()
    print("--------------------------------------")
    print("MAX HEAP AFTER DELETION:")
    MH.print_heap()
    print("--------------------------------------")
    max_val = MH.get_max()
    print("\nMAXIMUM ELEMENT IN HEAP AFTER DELETION:", max_val)
    print("=======================================")

    sorted_elements = MH.heap_sort()
    print("\nSORTING USING HEAP SORT:", sorted_elements)
    print("========================")

main()
