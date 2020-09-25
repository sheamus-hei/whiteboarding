#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Brute force: loop through the list N times and add up all the numbers
def add_to_k(numbers, k):
# for (let i = 0; i < numbers.length; i++)
  for i in range(len(numbers) - 1):
    current = numbers[i]
    for j in range(i + 1, len(numbers)):
      print("checking", current, "+", numbers[j])
      if current + numbers[j] == k:
        return True
  return False    

def add_to_k_recursive(numbers, num):
  if (len(numbers) < 2):
    return False
  elif numbers[0] + numbers[-1] == num:
    return True
  else:
    return add_to_k_recursive(numbers[:-1], num) or add_to_k_recursive(numbers[1:], num)

numList = [10, 15, 3, 7]
k = 10

print(add_to_k(num_list, k))
print(add_to_k_recursive(numList, k))
