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
  

# prints the parent before each child
def pre_order(node):
  if node:
    print(node.value)
    pre_order(node.left)
    pre_order(node.right)

# prints children and then parent
def post_order(node):
  if node:
    post_order(node.left)
    post_order(node.right)
    print(node.value)

# prints left child, parent, then right child
def in_order(node):
  if node:
    in_order(node.left)
    print(node.value)
    in_order(node.right)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

print("PRE-ORDER")
pre_order(tree)
print("POST-ORDER")
post_order(tree)
print("IN-ORDER")
in_order(tree)

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
