# Problem from LeetCode: https://leetcode.com/problems/symmetric-tree/
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
#          1
#         / \
#        2   2
#      / \   / \
#     3   4 4   3
# -> True

# Example 2:
#          1
#         / \
#        2   2
#      /    / 
#     3    3
# -> False

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
def is_mirror(root):
  return check_halves(root.left, root.right)

def check_halves(left, right):
  if not left and not right:
    return True
  if left and right:
    if left.data == right.data:
      left_half = check_halves(left.left, right.right) 
      right_half = check_halves(left.right, right.left)
      return left_half and right_half
  return False

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(2)
tree1.left.left = TreeNode(3)
tree1.right.right = TreeNode(3)
tree1.left.right = TreeNode(4)
tree1.right.left = TreeNode(4)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(2)
tree2.left.left = TreeNode(3)
tree2.right.left = TreeNode(3)

print(is_mirror(tree1))
print(is_mirror(tree2))
