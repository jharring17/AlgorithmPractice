# Recursive
# Finds the closest value in a binary search tree.
# Average Time Complexity: O(log(n)) where n is node number, Space Complexity: O(log(n))
#   Worst Case: Single branch -> O(n) Time, O(n) Space
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
    # Base case: there is no tree.
    if (tree is None):
        return closest
    # Potential update of closest.
    if (abs(target - closest) > abs(target - tree.value)):
        closest = tree.value
    # On left side of tree.
    if (target < tree.value):
        return findClosestValueInBSTHelper(tree.left, target, closest)
    # On right side of tree.
    elif (target > tree.value):
        return findClosestValueInBSTHelper(tree.right, target, closest)
    # Return closest.
    else:
        return closest

# This is the class of the input tree. 
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
