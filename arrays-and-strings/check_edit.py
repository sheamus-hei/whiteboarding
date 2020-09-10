# There are three types of edits that can be performed on a string: insert, remove, or replace one character. Given  two srings, write a function to check if they are 1 or less edits away from each other.

# pale, pal -> True
# pale, pales -> True
# pale, pa -> False
# apale, abale -> True

def check_edit(str1, str2):
  index2 = 0
  for letter in str1:
    if letter != str2[index2]:
      # figure out what kind of edit
      # check missing letter
      missing = str1[:index2] + str1[index2 + 1:]
      if (missing == str2):
        # return "removal"
        return True
      # check replaced letter
      replaced = str1[:index2] + str2[index2] + str1[index2 + 1:]
      if (replaced == str2):
        # return "replacement"
        return True
      # check added letter
      added = str1[:index2] + str2[index2] + str1[index2:]
      if (added == str2):
        # return "addition"
        return True
    else:
      index2 += 1
      if index2 == len(str2) and len(str1) == len(str2) + 1 or len(str1) == len(str2):
        # return "addition"
        return True
      elif index2 >= len(str2):
        return False
  if len(str2) - 1 == len(str1):
    # return "addition"
    return True
  return False

print(check_edit("pale", "bale"))
# -> True