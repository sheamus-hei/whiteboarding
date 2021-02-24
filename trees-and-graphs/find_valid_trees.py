# Given a root node, return a list of valid trees in that tree. 

#              a
#            /   \
#           b*    c
#          / \   / \
#         d  e  f*  g
#        /
#       h

# * = could be deleted
# in the above example, valid trees are
# a-c-g, d-h, e

# Approach
# 1. traverse the entire tree to look for deleted nodes and push children into the list of valid trees
# 2. For each valid tree, go through and remove "dead" nodes
# 3. return valid tree list

# tree node class
class TreeNode:
  def __init__(self, value, delete):
    self.value = value
    self.delete = delete or False
    self.left = None
    self.right = None

# main method
def find_valid_trees(root):
  valid_trees = [root]
  find_children(root, valid_trees)
  # for node in valid_trees:
  #   print(node.value)
  for tree in valid_trees:
    remove_deleted(tree)

  return valid_trees

# find top node of valid trees
def find_children(node, tree_list):
  if node:
    if node.delete:
      if node.left:
        tree_list.append(node.left)
      if node.right:
        tree_list.append(node.right)
    find_children(node.left, tree_list)
    find_children(node.right, tree_list)
  return
    
# remove deleted nodes from tree
def remove_deleted(node):
  if node:
    if node.right and node.right.delete:
      node.right = None
    if node.left and node.left.delete:
      node.left = None
    remove_deleted(node.right)
    remove_deleted(node.left)
  return

# prints the pre-order traversal of tree
def pre_order(node):
  if node:
    print(node.value)
    pre_order(node.left)
    pre_order(node.right)

tree = TreeNode("a", False)
tree.left = TreeNode("b", True)
tree.right = TreeNode("c", False)
tree.left.left = TreeNode("d", False)
tree.left.right = TreeNode("e", False)
tree.right.left = TreeNode("f", True)
tree.right.right = TreeNode("g", False)
tree.left.left.left = TreeNode("h", False)

# pre_order(tree)
trees = find_valid_trees(tree)
for valid_tree in trees:
  pre_order(valid_tree)
  print('[end]')
