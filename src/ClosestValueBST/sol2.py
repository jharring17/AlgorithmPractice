# Iterative
# Finds the closest value in a binary search tree.
# Average Time Complexity: O(log(n)) where n is node number, Space Complexity: O(1)
#   Worst Case: Single branch -> O(n) Time, O(1) Space
# 
# Binary Search Tree:
#                10
#              /    \
#             5      15
#           /   \   /  \
#          2     5 13   22
#         /          \
#        1           14

def findClosestValueInBst(tree, target):
    return findClosestValueInBSTHelper(BST, target, tree.value)

def findClosestValueInBSTHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        # Potential update of closest.
        if (abs(target - closest) > abs(target - currentNode.value)):
            closest = currentNode.value
        # On left side of tree.
        elif (target < currentNode.value):
            currentNode = currentNode.left
        # On right side of tree.
        elif (target > currentNode.value):
            currentNode = currentNode.right
        # Return closest.
        else:
            break
    return closest

# This is the class of the input tree. 
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
