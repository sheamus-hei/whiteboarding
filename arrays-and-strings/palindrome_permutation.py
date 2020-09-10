# Given a string, write a funciton to check if it is a permutation of a palindrome. A palindrome does not to be limited to just dictionary words. You can ignore casing and non-letter characters.

# taccota -> return True
# tacocat
# aaccott

def check_pali(our_string):
  our_string = our_string.lower()
  counts = {}
  for letter in our_string:
    if letter in counts.keys():
      counts[letter] += 1
    # elif letter in "abcdefghijklmnopqrstuvwxyz":
    elif ord(letter) >= 97 and ord(letter) <= 122:
      counts[letter] = 1
  middle = ""
  for letter in counts:
    if middle and counts[letter] % 2 == 1:
      return False
    elif counts[letter] % 2 == 1:
      middle = letter
  return True
#   # bonus: return a possible palindrome
#   if middle:
#     new_pali = middle * counts[middle]
#   else:
#     new_pali = ""
#   for letter in counts:
#     if letter != middle:
#       new_pali = letter * int(counts[letter] / 2) + new_pali + letter * int(counts[letter] / 2) 
#       pass
#   return new_pali

print(check_pali("Eva, can I stab bats in a cave?"))
# -> True
