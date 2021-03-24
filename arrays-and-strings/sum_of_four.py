# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# a + b + c + d = target

# Notice that the solution set must not contain duplicate quadruplets.

# Example 1:

# Input: nums = [1,0,-1,0,-2,2, 0], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:

# Input: nums = [], target = 0
# Output: []


def sum_of_four(nums, target):
  if len(nums) < 4:
    return []
  output = []
  nums.sort()
  checked = set()
  for i in range(len(nums) - 3):
    working_target = target - nums[i]
    current = [nums[i]]
    for j in range(i + 1, len(nums) - 2):
      working_target -= nums[j]
      current.append(nums[j])
      for k in range(j + 1, len(nums) - 1):
        working_target -= nums[k]
        current.append(nums[k])
        for m in range(k + 1, len(nums)):
          current.append(nums[m])
          if working_target - nums[m] == 0:
            # make code to put in duplicate set
            code = str(current[0])
            for n in range(1, len(current)):
              code += "&" + str(current[n])
            if code not in checked:
              output.append(current.copy())
              checked.add(code)
          current.pop()
        current.pop()
        working_target += nums[k]
      current.pop()
      working_target += nums[j]

  return output

#def sum_of_four_recursive(nums, target)

  
nums = [1,0,-1,0,-2,2, 0]
target = 0
print(sum_of_four(nums, target))