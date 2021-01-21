# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","hat","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def find_longest_prefix(words):
  prefix = ""
  for i in range(len(words[0])):
    letter = words[0][i]
    for j in range(1, len(words)):
      if (i >= len(words[j])) or (letter != words[j][i]):
        return prefix
    prefix = prefix + letter
  return prefix

strs = ["flower","flow","flood"]
# strs = ["dog","cat","car"]
print(find_longest_prefix(strs))