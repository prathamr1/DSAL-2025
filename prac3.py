class SetADT:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, element):
        return hash(element) % self.capacity

    def add(self, element):
        index = self._hash(element)
        bucket = self.buckets[index]

        if element in bucket:
            print(f"{element} already exists.")
            return

        bucket.append(element)
        self.size += 1
        print(f"Added: {element}")

    def remove(self, element):
        index = self._hash(element)
        bucket = self.buckets[index]

        try:
            bucket.remove(element)
            self.size -= 1
            print(f"Removed: {element}")
        except ValueError:
            print(f"{element} not found in set.")

    def contains(self, element):
        index = self._hash(element)
        bucket = self.buckets[index]
        return element in bucket

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        print("Set cleared.")

    def get_size(self):
        return self.size

    def to_list(self):
        result = []
        for bucket in self.buckets:
            result.extend(bucket)
        return result

    def union(self, other_set):
        result = SetADT()
        for item in self.to_list():
            result.add(item)
        for item in other_set.to_list():
            result.add(item)
        return result

    def intersection(self, other_set):
        result = SetADT()
        for item in self.to_list():
            if other_set.contains(item):
                result.add(item)
        return result

    def difference(self, other_set):
        result = SetADT()
        for item in self.to_list():
            if not other_set.contains(item):
                result.add(item)
        return result

    def is_subset(self, other_set):
        for item in self.to_list():
            if not other_set.contains(item):
                return False
        return True

    def __str__(self):
        return "{" + ", ".join(str(x) for x in self.to_list()) + "}"


# 🧪 Example Usage
if __name__ == "__main__":
    A = SetADT()
    A.add(1)
    A.add(2)
    A.add(3)
    A.add(2)  # Duplicate

    B = SetADT()
    B.add(3)
    B.add(4)
    B.add(5)

    print("\nSet A:", A)
    print("Set B:", B)

    print("\nUnion:", A.union(B))
    print("Intersection:", A.intersection(B))
    print("Difference A - B:", A.difference(B))
    print("Is A subset of B?", A.is_subset(B))

    A.remove(2)
    print("After removing 2 from A:", A)

    print("Does A contain 1?", A.contains(1))
    print("Set A size:", A.get_size())
    A.clear()
    print("Set A after clearing:", A)
