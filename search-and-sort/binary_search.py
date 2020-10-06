# a binary search allows us to search for an element in a sorted array.
# this is more efficient than a loop because the time complexity is O(logN) instead of O(N).

def search2(nums, value, lo, hi):
  if lo > hi:
    return None # not in list
  mid = (lo + hi) // 2
  if (nums[mid] < value): # look in upper half
    return search2(nums, value, mid + 1, hi)
  elif (nums[mid] > value): # look in lower half
    return search2(nums, value, lo, mid - 1)
  else: # if value == nums[mid]
    return mid

def binary_search(nums, value):
  lo = 0
  hi = len(nums) - 1
  return search2(nums, value, lo, hi)

# >>> binary_search([1,2,3], 2)
# 1
