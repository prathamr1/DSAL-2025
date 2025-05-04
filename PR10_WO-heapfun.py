class Heap:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

    def extract(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        root = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.data[index] < self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == index:
                break
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

if __name__ == "__main__":
    marks = list(map(int, input("Enter marks of students (space-separated): ").split()))
    if not marks:
        print("No marks entered.")
    else:
        min_heap = Heap()
        max_heap = Heap()
        
        for mark in marks:
            min_heap.insert(mark)
            max_heap.insert(-mark)  # Inverting values for max-heap
        
        min_marks = min_heap.extract()
        max_marks = -max_heap.extract()
        
        print(f"Minimum Marks: {min_marks}")
        print(f"Maximum Marks: {max_marks}")
