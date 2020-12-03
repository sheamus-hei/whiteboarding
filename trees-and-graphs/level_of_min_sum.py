
# Given a binary tree, return the level of the tree with minimum sum.

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# example of pre order traversal
def pre_order(node):
  if node:
    print(node.value)
    pre_order(node.left)
    pre_order(node.right)

# method to find how tall a tree is
def height(node):
  if not node:
    return 0
  l_height = height(node.left)
  r_height = height(node.right)
  if l_height > r_height:
    return l_height + 1
  return r_height + 1

# following two methods print breadth first traversal
def print_given_level(root, level):
  if not root:
    return
  if level == 1:
    print(root.value, end=" ")
  elif level > 1:
    print_given_level(root.left, level-1)
    print_given_level(root.right, level-1)

def print_level_order(root):
  h = height(root)
  for i in range(1, h+1):
    print_given_level(root, i)

# following two methods are for the interview question
def traverse_levels(root, level):
  if not root:
    return 0
  if level == 1:
    return root.value
  elif level > 1:
    return traverse_levels(root.left, level-1) + traverse_levels(root.right, level-1)

def level_min_sum(root):
  h = height(root)
  min = root.value
  level = 1
  for i in range(1, h+1):
    current_min = traverse_levels(root, i)
    if current_min < min:
      min = current_min
      level = i
  return level


root = TreeNode(2)
root.left = TreeNode(7)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(11)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(4)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# pre_order(root)
print("Height:", height(root))
print(level_min_sum(root))
