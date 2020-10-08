# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
  def print_node(self):
    print(self.value)

 # prints the nodes from the leaves up
def post_order(node):
  if node:
    post_order(node.left)
    post_order(node.right)
    node.print_node()

def unival_trees(node, count):
  if node:
    left = unival_trees(node.left, count)
    right = unival_trees(node.right, count)
    if not left or not right:
      return False
    if node.left and node.left.value != node.value:
      return False
    if node.right and node.right.value != node.value:
      return False
    count[0] += 1
    return True
  return True

def count_trees(node):
  count = [0]
  unival_trees(node, count)
  return count[0]

tree = TreeNode(0)
tree.left = TreeNode(1)
tree.right = TreeNode(0)
tree.right.left = TreeNode(1)
tree.right.right = TreeNode(0)
tree.right.left.left = TreeNode(1)
tree.right.left.right = TreeNode(1)

print(count_trees(tree))
# -> 5
