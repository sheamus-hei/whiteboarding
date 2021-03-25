# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
from collections import defaultdict
def validate_ransom(note, magazine):
  if len(note) > len(magazine):
    return False
  counts = defaultdict(int)
  for letter in magazine:
    counts[letter] += 1
  for letter in note:
    if counts[letter] <= 0:
      return False
    else:
      counts[letter] -= 1
  return True
  
# Time: O(M + N)
# Space: O(1) "constant" (26 letters)
note = "helloz"
magazine = "efjklfehlseo"
print(validate_ransom(note, magazine))