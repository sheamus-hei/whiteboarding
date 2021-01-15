
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false     

def find_iso(s, t):
  reviewed = set()
  for i in range(len(s)):
    if s[i] not in reviewed:
      current_s = s[i]
      current_t = t[i]
      for j in range(i + 1, len(s)):
        if s[j] == current_s and t[j] != current_t:
          print(current_s, current_t)
          return False
      reviewed.add(current_s)
  return True


s = 'title'
t = 'paler'
print(find_iso(s, t))