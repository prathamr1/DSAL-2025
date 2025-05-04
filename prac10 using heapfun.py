import heapq

def find_min_max_marks(marks):
    if not marks:
        return None, None
    
    min_heap = marks[:]
    max_heap = [-mark for mark in marks]
    
    heapq.heapify(min_heap)  # Min heap for minimum marks
    heapq.heapify(max_heap)  # Max heap (inverted) for maximum marks
    
    min_marks = heapq.heappop(min_heap)
    max_marks = -heapq.heappop(max_heap)
    
    return min_marks, max_marks

if __name__ == "__main__":
    marks = list(map(int, input("Enter marks of students (space-separated): ").split()))
    min_marks, max_marks = find_min_max_marks(marks)
    
    if min_marks is not None and max_marks is not None:
        print(f"Minimum Marks: {min_marks}")
        print(f"Maximum Marks: {max_marks}")
    else:
        print("No marks entered.")