# Given a string, write a funciton to check if it is a permutation of a palindrome. A palindrome does not to be limited to just dictionary words. You can ignore casing and non-letter characters.

# "taco cat" -> return True
# "cat" -> return False

from collections import defaultdict

def check_pali(our_string):
  our_string = our_string.lower()
  counts = defaultdict(int)
  for letter in our_string:
    if ord(letter) >= 97 and ord(letter) <= 122:
      counts[letter] += 1 
  # print(counts)
  middle = ""
  for letter in counts:
    if middle and counts[letter] % 2 == 1:
      return False
    elif counts[letter] % 2 == 1:
      middle = letter
  # return True
  # bonus: return a possible palindrome
  new_pali = ""
  if middle:
    new_pali = middle * counts[middle]
  for letter in counts:
    if letter != middle:
      new_pali = letter * int(counts[letter] / 2) + new_pali + letter * int(counts[letter] / 2) 
  return new_pali

print(check_pali("Eva can I stab bats in a cave"))
# -> True
print(check_pali("tacocat"))
# -> False