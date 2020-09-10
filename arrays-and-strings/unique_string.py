# Determine if a string has all unique characters. 
# You cannot use additional data structures.

# brute force: nested for loop
def is_unique(our_string):
  for i in range(len(our_string) - 1):
    for j in range(i + 1, len(our_string)):
      if our_string[j] == our_string[i]:
        return False
  return True

# more optimal: sort the string
def is_unique2(our_string):
  str_list = [char for char in our_string]
  str_list.sort()
  last = ""
  for letter in str_list:
    if letter == last:
      return False
    else: 
      last = letter
  return True


print(is_unique2("hello"))
# -> False
#print(is_unique("hi"))
# -> True