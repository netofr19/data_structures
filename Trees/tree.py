from collections import deque

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left)
    print(current.data)
    inorder(current.right)

def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left)
    preorder(current.right)

def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left)
    postorder(current.right)
    print(current.data)

def level_order_traversal(root_node):
    list_of_nodes = []
    traversal_queue = deque([root_node])
    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()
        list_of_nodes.append(node.data)
        if node.left:
            traversal_queue.append(node.left)
            if node.right:
                traversal_queue.append(node.right)
    return list_of_nodes


if __name__ == '__main__':
    n1 = Node("root node")
    n2 = Node("left child node")
    n3 = Node("right child node")
    n4 = Node("left grandchild node")

    n1.left = n2
    n1.right = n3
    n2.left = n4

    print("---- In Order ----")
    inorder(n1)

    print("\n---- Pre Order ----")
    preorder(n1)

    print("\n---- Post Order ----")
    postorder(n1)

    print("\n---- Level Order Traversal ----")
    print(level_order_traversal(n1))
