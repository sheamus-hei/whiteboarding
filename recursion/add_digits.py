# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:

# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#             Since 2 has only one digit, return it.


def add_digits(num):
  if num/10 < 1:
    return num
  else:
    # cast to string
    num = str(num)
    sum = 0
    # add the digits together
    for digit in num:
      print(digit)
      sum += int(digit)
    # call recursive function
    # print(sum)
    return add_digits(sum)

print(add_digits(38))
    