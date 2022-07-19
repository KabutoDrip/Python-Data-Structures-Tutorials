class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def delete_Node(root, data):
        if not root: 
            return root
        if root.data > data: 
            root.left = Node.delete_Node(root.left, data)
        elif root.data < data: 
            root.right= Node.delete_Node(root.right, data)
        else: 
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            temp_data = root.right
            while temp_data.left:
                temp_data = temp_data.left
            root.right = Node.delete_Node(root.right,root.data)
        return root
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def ordered_traversal(self, root):
        res = []
        if root:
            res = self.ordered_traversal(root.left)
            res.insert(root.data)
            res = res + self.ordered_traversal(root.right)
            if root.data.find(".jar") == 1:
                self.delete_Node(root)

        return res

root = Node("hello.png")
root.insert("stacks.py")
root.insert("sets.py")
root.insert("trees.py")
root.insert("index.html")
root.insert("sketch.jar")
root.insert("hello.jpeg")
print(root.ordered_traversal(root))