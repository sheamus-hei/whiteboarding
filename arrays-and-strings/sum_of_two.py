# Given an array nums of n integers and an integer target, are there elements a and b 
# such that a + b = target

# Notice that the solution set must not contain duplicate pairs.

# Example 1:

# Input: nums = [1,0,-1,0,-2,2, 0], target = 0
# Output: [[-2,2],[1, -1],[0, 0]]

# Example 2:

# Input: nums = [], target = 0
# Output: []


def sum_of_two(nums, target):
  if len(nums) < 2:
    return []
  output = []
  nums.sort()
  checked = set()
  for i in range(len(nums) - 1):
    working_target = target - nums[i]
    current = [nums[i]]
    for j in range(i + 1, len(nums)):
      current.append(nums[j])
      if working_target - nums[j] == 0:
        # make code to put in duplicate set
        code = str(current[0])
        for number in range(1, len(current)):
          code += "&" + str(number)
        if code not in checked:
          print(current)
          output.append(current.copy())
          checked.add(code)
      current.pop()
  return output
 

  
nums = [1,0,-1,0,-2,2, 0]
target = 0
print(sum_of_two(nums, target))