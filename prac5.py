class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to check if a character is an operator
def is_operator(c):
    return c in "+-*/"


# Operator precedence
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


# Convert infix expression to postfix using Shunting Yard Algorithm
def infix_to_postfix(expression):
    stack = []
    output = []
    for token in expression:
        if token.isalnum():  # Operand
            output.append(token)
        elif is_operator(token):  # Operator
            while (stack and precedence(stack[-1]) >= precedence(token)):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output


# Build expression tree from postfix
def build_expression_tree(postfix):
    stack = []
    for token in postfix:
        node = TreeNode(token)
        if is_operator(token):
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack[-1]


# Inorder traversal (recursive)
def inorder(node):
    if node:
        if is_operator(node.value):
            print("(", end="")
        inorder(node.left)
        print(node.value, end="")
        inorder(node.right)
        if is_operator(node.value):
            print(")", end="")


# Postorder traversal (non-recursive using two stacks)
def postorder_non_recursive(root):
    if not root:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    print("\nPostorder Traversal (non-recursive):")
    while stack2:
        print(stack2.pop().value, end=" ")


# Main function
if __name__ == "__main__":
    expression = "a-b*c-d/e+f"
    print("Given Expression:", expression)

    postfix = infix_to_postfix(expression)
    print("Postfix Expression:", " ".join(postfix))

    root = build_expression_tree(postfix)

    print("\nInorder Traversal (expression format):")
    inorder(root)

    postorder_non_recursive(root)
