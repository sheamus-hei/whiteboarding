# basic class
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


#       1
#     /   \
#    2     3
#   / \    
#  4   5

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

# Depth first traversal: 
# print first for pre-order, middle for in-order, last for post-order
# prints the parent before each child
def traversal(node):
  if node:
    print(node.value)
    traversal(node.left)
    traversal(node.right)

traversal(tree)

# Breadth first traversal: more complicated

# method to find how tall a tree is
def height(node):
  if not node:
    return 0
  l_height = height(node.left)
  r_height = height(node.right)

  return max(l_height, r_height) + 1

# following two methods print breadth first traversal
# source: https://www.geeksforgeeks.org/level-order-tree-traversal/
def print_level(root, level):
  if not root:
    return
  if level == 0:
    print(root.value)
  elif level > 0:
    print_level(root.left, level - 1)
    print_level(root.right, level - 1)

def breadth_first(root):
  h = height(root)
  for i in range(h):
    print_level(root, i)

# write a function that counts the total number of nodes in the tree.
def count_nodes(node):
  if not node:
    return 0
  else:
    return 1 + count_nodes(node.left) + count_nodes(node.right)

print("There are", count_nodes(tree), "nodes in the tree")

# write a function that finds the minimum value in a tree.
import sys
def find_min(node):
  if not node:
    return sys.maxsize
  else:
    left_min = min(node.value, find_min(node.left))
    right_min = min(node.value, find_min(node.right))
    return min(left_min, right_min)

# tree.left.left.left = TreeNode(0)
traversal(tree)
print("Min node:", find_min(tree))