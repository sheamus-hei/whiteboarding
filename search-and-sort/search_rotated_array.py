# An sorted array of integers was rotated an unknown number of times.
# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
# You can assume all the integers in the array are unique.

# use a modified binary search

def find_index(lis, value, left, right):
  mid = (left + right) // 2
  if lis[mid] == value:
    return mid
  elif lis[left] == lis[mid] and lis[mid] == lis[right]:
    return None
  # check lower half
  elif lis[left] <= value and value < lis[mid]:
    return find_index(lis, value, left, mid)
  # check upper half
  elif lis[mid] < value and value <= lis[right]:
    return find_index(lis, value, mid, right)
  # move the mid up or down
  elif lis[left] > lis[mid]:
    return find_index(lis, value, left, mid - 1)
  else: # if lis[mid] > lis[right]
    return find_index(lis, value, mid + 1, right)


def find_rotated_index(lis, value):
  return find_index(lis, value, 0, len(lis)-1)

print(find_rotated_index([17,18,19,2,3], 1))
# -> None
print(find_rotated_index([17,18,19,2,3], 18))
# -> 1
print(find_rotated_index([17,18,19,2,3], 19))
# -> 2
print(find_rotated_index([17,18,19,2,3], 2))
# -> 3