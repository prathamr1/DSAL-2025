class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        print("    " * level + f"- {self.name}")
        for child in self.children:
            child.print_tree(level + 1)


def build_book_tree():
    # Root of the tree (the book)
    book = TreeNode("Book Title")

    # Chapter 1
    chapter1 = TreeNode("Chapter 1")
    section1_1 = TreeNode("Section 1.1")
    section1_2 = TreeNode("Section 1.2")

    subsection1_1_1 = TreeNode("Subsection 1.1.1")
    subsection1_1_2 = TreeNode("Subsection 1.1.2")
    section1_1.add_child(subsection1_1_1)
    section1_1.add_child(subsection1_1_2)

    subsection1_2_1 = TreeNode("Subsection 1.2.1")
    section1_2.add_child(subsection1_2_1)

    chapter1.add_child(section1_1)
    chapter1.add_child(section1_2)

    # Chapter 2
    chapter2 = TreeNode("Chapter 2")
    section2_1 = TreeNode("Section 2.1")
    subsection2_1_1 = TreeNode("Subsection 2.1.1")
    section2_1.add_child(subsection2_1_1)
    chapter2.add_child(section2_1)

    # Add chapters to the book
    book.add_child(chapter1)
    book.add_child(chapter2)

    return book


if __name__ == "__main__":
    book = build_book_tree()
    print("Book Structure:\n")
    book.print_tree()
