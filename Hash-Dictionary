class HashNode:
    """A node in the linked list for separate chaining in hash table"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """Hash Table implementing Dictionary ADT"""
    def __init__(self, capacity=10):
        self.capacity = capacity         
        self.size = 0                     
        self.buckets = [None] * capacity  

    def _hash(self, key):
        """Hash function to get the bucket index"""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Insert or update a key-value pair in the hash table"""
        index = self._hash(key)
        head = self.buckets[index]

        # Check if key exists and update
        current = head
        while current:
            if current.key == key:
                current.value = value
                print(f"Updated: ({key}, {value})")
                return
            current = current.next

        # Insert new node at the beginning
        new_node = HashNode(key, value)
        new_node.next = head
        self.buckets[index] = new_node
        self.size += 1
        print(f"Inserted: ({key}, {value})")

    def find(self, key):
        """Find the value associated with a key"""
        index = self._hash(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                print(f"Found: ({key}, {current.value})")
                return current.value
            current = current.next

        print(f"Key '{key}' not found.")
        return None

    def delete(self, key):
        """Delete a key-value pair by key"""
        index = self._hash(key)
        current = self.buckets[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                self.size -= 1
                print(f"Deleted: {key}")
                return True
            prev = current
            current = current.next

        print(f"Key '{key}' not found for deletion.")
        return False

    def __str__(self):
        """Return a string representation of the hash table"""
        output = []
        for i in range(self.capacity):
            current = self.buckets[i]
            while current:
                output.append(f"{current.key}: {current.value}")
                current = current.next
        return "{ " + ", ".join(output) + " }"

# Example Usage
if __name__ == "__main__":
    d = HashTable()

    # Insert key-value pairs
    d.insert("apple", 10)
    d.insert("banana", 20)
    d.insert("orange", 30)
    d.insert("apple", 15)  # Update value for "apple"

    # Display the dictionary
    print("\nCurrent Dictionary:")
    print(d)

    # Find values
    d.find("banana")
    d.find("grape")  # Not found

    # Delete a key
    d.delete("banana")
    d.delete("grape")  # Not found

    # Final dictionary
    print("\nFinal Dictionary:")
    print(d)
