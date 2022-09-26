# BFS Implementation in Python

# Node class definition.
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
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

# Populates a Tree.
root = Node('g')
tree_elements = ['c', 'b', 'a', 'e', 'd', 'f', 'i', 'h', 'j', 'k']
for element in tree_elements:
    root.insert(element)

# Print the nodes in an in-order traversal.
