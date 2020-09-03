# a binary search allows us to search for an element in a sorted array.
# this is more efficient than a loop because the time complexity is O(logN) instead of O(N).

def search2(lis, value, lo, hi):
  if lo > hi:
    return None # not in list
  mid = (lo + hi) // 2
  if (lis[mid] < value): # look in upper half
    return search2(lis, value, mid + 1, hi)
  elif (lis[mid] > value): # look in lower half
    return search2(lis, value, lo, mid - 1)
  else: # if value == lis[mid]
    return mid

def binary_search(lis, value):
  lo = 0
  hi = len(lis) - 1
  return search2(lis, value, lo, hi)

# >>> binary_search([1,2,3], 2)
# 1
