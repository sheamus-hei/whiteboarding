class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

#  1
# / \
#2.  3

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)

def print_nodes(root):
  if root:
    print(root.data)
    print_nodes(root.left)
    print_nodes(root.right)


# print_nodes(tree)

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).



# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Example 2:

# Input: root = [1,2,3]
# Output: [1,3]
# Example 3:

# Input: root = [1]
# Output: [1]
# Example 4:

# Input: root = [1,null,2]
# Output: [1,2]
# Example 5:

# Input: root = []
# Output: []

# method to find how tall a tree is
def height(node):
  if not node:
    return 0
  l_height = height(node.left)
  r_height = height(node.right)

  return max(l_height, r_height) + 1

# following two methods print breadth first traversal
# source: https://www.geeksforgeeks.org/level-order-tree-traversal/
def evaluate_level(root, level, max):
  if not root:
    return
  print("node", root.data, "level tracker", level)
  if level == 0:
    if root.data > max[0]:
      max[0] = root.data
  elif level > 0:
    evaluate_level(root.left, level - 1, max)
    evaluate_level(root.right, level - 1, max)

import sys
def find_largest_val(root):
  h = height(root)
  output = []
  for i in range(h):
    print("i equals", i)
    current_max = [-sys.maxsize]
    evaluate_level(root, i, current_max)
    output.append(current_max[0])
  return output

# Input: root = [1,3,2,5,3,null,9]
tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.left.left = Node(5)
tree.left.right = Node(3)
tree.right.right = Node(9)
print(find_largest_val(tree))