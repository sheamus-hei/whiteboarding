
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.


# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0


def find(s, backwards):
  curr_s = ""
  count = 0
  max = 0
  key = {
    "(": 1 - int(backwards) * 2,
    ")": -1 + int(backwards) * 2
  }
  for i in range(len(s)):
    value = s[i] #(
    if backwards: 
      value = s[-i]
    count += key[value] # +1 = 1
    # print(value, count, curr_s)
    if count < 0:
      # reset
      curr_s = ""
      count = 0
    else:
      curr_s += value
      # evaluate
      if count == 0 and len(curr_s) > max:
        max = len(curr_s)
  return max

def longest_paren(s):
  if len(s) < 2:
    return 0
  return max(find(s, True), find(s, False))

print(longest_paren("((())()"))
