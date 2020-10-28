# This is a sample problem from an intro to JS course that I tried to convert to python.

# A number is pandigital if it has digits 1-n for a number n digits long.
# Given a number, return whether or not it is pandigital.

# function isPandigital(num) {
#   num = num.toString().split("").sort()
#   console.log(num)
#   for (let i=0; i < num.length; i++) {
#     if (num[i] != i+1) {
#       return false
#     }
#   }
#   return true
# }

# isPandigital(127354)

def is_pandigital(num):
  num = [digit for digit in str(num)]
  num.sort()
  print(num)
  for i in range(len(num)):
    if int(num[i]) != (i + 1):
      return False
  return True

# more optimal time 
def is_pandigital2(num):
  num = str(num)
  counter = [False] * len(num)
  for digit in num:
    digit = int(digit)
    if digit > len(num) or counter[digit - 1]:
      print(counter)
      return False
    else:
      counter[digit - 1] = True
  print(counter)
  return True

# other O(N) solution using a set
def is_pandigital3(num):
  num = str(num)
  s1 = set()
  s2 = set()
  for n in range(len(num)):
    s1.add(n+1)
    s2.add(int(num[n]))
  return s1 == s2



print(is_pandigital(321))
# -> True
print(is_pandigital2(123465))
# -> True
print(is_pandigital3(12765))
# -> False


 