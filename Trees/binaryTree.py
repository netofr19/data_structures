class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class BinaryTree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return self.root_node
                elif node.data > parent.data:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return self.root_node
                else:
                    return self.root_node
                
    def inorder(self, root_node):
        current = root_node
        if current is None:
            return None
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def search(self, data):
        current = self.root_node
        position = []
        while True:
            if current is None:
                print('Item not found!')
                return None
            elif current.data == data:
                print(f"Item found...: {data}")
                return position
            elif current.data > data:
                current = current.left_child
                position.append('left')
            else:
                current = current.right_child
                position.append('right')

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node

        if current is None:
            return (parent, None)
        
        while current:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child

        return (parent, current)

if __name__ == '__main__':
    tree = BinaryTree()

    r = tree.insert(5)
    r = tree.insert(2)
    r = tree.insert(7)
    r = tree.insert(9)
    r = tree.insert(1)

    pos = tree.search(9)
    print(f'Path: {pos}')


