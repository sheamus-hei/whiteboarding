# Determine if a string has all unique characters. 
# You cannot use additional data structures.

# brute force: nested for loop
def is_unique(s):
  for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
      if s[j] == s[i]:
        return False
  return True

# more optimal: sort the string
def is_unique2(s):
  s_as_list = [char for char in s]
  s_as_list.sort()
  prev = ""
  for letter in s_as_list:
    if letter == prev:
      return False
    else: 
      prev = letter
  return True

# alternative: use a dictionary
from collections import defaultdict

def is_unique3(s):
  dd = defaultdict(bool)
  for char in s:
    if dd[char]:
      return False
    dd[char] = True
  return True



print(is_unique2("hello"))
# -> False
#print(is_unique("hi"))
# -> True