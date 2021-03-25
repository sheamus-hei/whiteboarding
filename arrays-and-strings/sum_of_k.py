# Given an array nums of n integers and an integer target, are there k elements 
# such that numbers n_1, n_2,..., n_k sum to the target?

# Notice that the solution set must not contain duplicate sets of k.

# Example 1:

# Input: nums = [1,0,-1,0,-2,2, 0], target = 0, k = 4
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:

# Input: nums = [], target = 0
# Output: []

# def coin_flips(n):
#   if n <= 1:
#     return ["H", "T"]
#   else:
#     flip_list = coin_flips(n-1)
#     print(flip_list)
#     new_list = []
#     for str in flip_list:
#       new_list.append(str+"H")
#       new_list.append(str+"T")
#     return new_list

def sum_of_k(nums, target, k):
  if len(nums) < k:
    return []
  output = []
  current = []
  nums.sort()
  checked = set()
  sum_helper(nums, target, k, output, checked, current, 0)
  return output

def sum_helper(nums, target, k, output, checked, current, prev):
  if k == 0:
    return
  for i in range(prev, len(nums) - k + 1):
    current.append(nums[i])
    if k == 1 and target - nums[i] == 0:
      # make code to put in duplicate set
      code = str(current[0])
      for n in range(1, len(current)):
        code += "&" + str(current[n])
      # print(code, current)
      if code not in checked:
        output.append(current.copy())
        checked.add(code)
    sum_helper(nums, target - nums[i], k - 1, output, checked, current, i + 1)
    current.pop()

nums = [-1,0,1,2,-1,-4, -2]
target = 0
k = 4
print(sum_of_k(nums, target, k))