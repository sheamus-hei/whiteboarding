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

print(is_pandigital(321))
# -> True
print(is_pandigital(123465))
# -> True
print(is_pandigital(12765))
# -> False


 