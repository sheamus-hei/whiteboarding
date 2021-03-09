
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []

from collections import defaultdict

def sum_of_three(nums):
  solutions = []
  seen = set()
  if len(nums) < 3:
    return solutions
  nums.sort()
  counts = defaultdict(int)
  for num in nums:
    counts[str(num)] += 1
  print(counts)
  for num in nums:
    num_counts = counts.copy()
    if num > 0:
      return solutions
    else:
      num_counts[str(num)] -= 1
      # check starting from end
      for i in range(1, len(nums)):
        second = nums[-i]
        # print("second", second)
        if second < 0:
          continue
        elif num_counts[str(second)] > 0:
          num_counts[str(second)] -= 1
          # look for third to make sum to zero
          third = 0 - num - second
          # print("third", third)
          # check if third in list
          code = str(num) + "#" + str(second) + "#" + str(third)
          if num_counts[str(third)] > 0 and code not in seen:
            seen.add(code)
            print(num)
            print(num_counts)
            solutions.append([num, second, third])
  return solutions
        

    
# {
#   "-4": 1,
#   "-1": 2,
#   "0": 1,
#   "1": 1,
#   "2": 1
# }
# -4  -> -4
# add 2 -> -2
# add 1 -> -1 #
# -1 -> -1
# add 2 -> 1
# add -1 -> 0 save
# -1 -> -1
# add 1 -> 0
# add 0 -> 0 save
# -1 #

nums = [-1,0,1, 2,-1,-4, 1, 3, 4, 2, -5, -2, -4]
print(sum_of_three(nums))


  