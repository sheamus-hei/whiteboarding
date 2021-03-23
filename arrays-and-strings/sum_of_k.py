# Given an array nums of n integers and an integer target, are there k elements 
# such that numbers n_1, n_2,..., n_k sum to the target?

# Notice that the solution set must not contain duplicate sets of k.

# Example 1:

# Input: nums = [1,0,-1,0,-2,2, 0], target = 0, k = 4
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:

# Input: nums = [], target = 0
# Output: []

def sum_of_k(nums, target, k):
  if len(nums) < k:
    return []
  output = []
  return sum_helper(nums, target, k, output)

def sum_helper(nums, target, k, output):
  pass

nums = [1,0,-1,0,-2,2, 0]
target = 0
k = 4
print(sum_of_four(nums, target, k))