class Node:
    def __init__(self, key, meaning):
        self.key = key
        self.meaning = meaning
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert(self, node, key, meaning):
        if not node:
            return Node(key, meaning)
        if key < node.key:
            node.left = self.insert(node.left, key, meaning)
        elif key > node.key:
            node.right = self.insert(node.right, key, meaning)
        else:
            node.meaning = meaning  # Update meaning if key exists010
            return node

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.get_balance(node)
        
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.min_value_node(node.right)
            node.key, node.meaning = temp.key, temp.meaning
            node.right = self.delete(node.right, temp.key)
        
        if not node:
            return node

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append((node.key, node.meaning))
            self.inorder_traversal(node.right, result)

    def search(self, node, key, comparisons=0):
        if not node:
            return None, comparisons
        comparisons += 1
        if key == node.key:
            return node.meaning, comparisons
        elif key < node.key:
            return self.search(node.left, key, comparisons)
        else:
            return self.search(node.right, key, comparisons)

if __name__ == "__main__":
    tree = AVLTree()
    root = None
    
    while True:
        print("\nMenu:")
        print("1. Add Keyword")
        print("2. Delete Keyword")
        print("3. Update Keyword")
        print("4. Display Dictionary (Sorted Order)")
        print("5. Search Keyword")
        print("6. Exit")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            key = input("Enter Keyword: ")
            meaning = input("Enter Meaning: ")
            root = tree.insert(root, key, meaning)
            print("Keyword Added Successfully.")

        elif choice == 2:
            key = input("Enter Keyword to Delete: ")
            root = tree.delete(root, key)
            print("Keyword Deleted Successfully.")

        elif choice == 3:
            key = input("Enter Keyword to Update: ")
            meaning = input("Enter New Meaning: ")
            root = tree.insert(root, key, meaning)  # Insert will update if key exists
            print("Keyword Updated Successfully.")

        elif choice == 4:
            result = []
            tree.inorder_traversal(root, result)
            print("Dictionary (Sorted Order):")
            for k, m in result:
                print(f"{k}: {m}")

        elif choice == 5:
            key = input("Enter Keyword to Search: ")
            meaning, comparisons = tree.search(root, key)
            if meaning:
                print(f"Meaning: {meaning}")
                print(f"Comparisons Required: {comparisons}")
            else:
                print("Keyword Not Found.")

        elif choice == 6:
            break
        else:
            print("Invalid Choice! Try Again.")
