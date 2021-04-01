# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time () to arrived late ().

# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

# Example

# k = 3
# a = [-2, -1, 0, 1, 2]

# The first 3 students arrived on. The last  were late. The threshold is 3 students, so class will go on. Return NO (not cancelled).

# Note: Non-positive arrival times (<= 0) indicate the student arrived early or on time; positive arrival times (> 0) indicate the student arrived  minutes late.

def angry_professor(min_students, arr_times):
  count = 0
  for time in arr_times:
    if time <= 0:
      count += 1
      if count >= min_students:
        return "NOT CANCELLED"
  return "CLASS CANCLELLED"

# modified binary search (includes helper method)
def search2(nums, value, lo, hi):
  if lo > hi:
    print("lo", lo, "hi", hi)
    if nums[hi] < 0:
      return hi
    else:
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

# assuming list is already sorted, better runtime at O(logN)
# including .sort() for consistency
# method does not work if more than one 0 in arr_times
def angry_professor2(min_students, arr_times):
  arr_times.sort()
  on_time_students = binary_search(arr_times, 0)
  print(on_time_students)
  if on_time_students >= min_students - 1:
    return "NOT CANCELLED"
  return "IS CANCELLED"

k = 3
a = [-2, 0, 3, 4, 5, -1, 2]

print(angry_professor2(k, a))
