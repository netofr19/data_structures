class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()
    
def calc(node):
    if node.data == "+":
        return calc(node.left) + calc(node.right)
    elif node.data == "-":
        return calc(node.left) - calc(node.right)
    elif node.data == "*":
        return calc(node.left) * calc(node.right)
    elif node.data == "/":
        return calc(node.left) / calc(node.right)
    else:
        return node.data
    
if __name__ == '__main__':
    expr = "4 5 + 5 3 - *".split()
    stack = Stack()

    for term in expr:
        if term in "+-*/":
            node = TreeNode(term)
            node.right = stack.pop()
            node.left = stack.pop()
        else:
            node = TreeNode(int(term))
        stack.push(node)

    root = stack.pop()
    result = calc(root)
    print(result)
