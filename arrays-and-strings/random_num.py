# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l(uniform).
import random
import math

# this method has infinite worst case complexity but average complexity is not bad 
# galaxy brain: keep rolling a new number until it's not in the list
# however no catch for if there are no possible numbers
def get_rand(n, nums):
  rand_num = math.floor(random.random() * n)
  s = set()
  for num in nums:
    s.add(num)
  while rand_num in s:
    print("reroll")
    rand_num = math.floor(random.random()*n)
  return rand_num

print(get_rand(7, [1,2,3]))

# alt approach to the above method using a recursive helper function (more complicated)
def find_rand(n, s):
  rand_num = math.floor(random.random()*n)
  if rand_num in s:
    print("reroll")
    return find_rand(n, s)
  return rand_num

def get_rand1(n, nums):
  s = set()
  for num in nums:
    s.add(num)
  return find_rand(n, s)

# more efficient, make a list of possible numbers and exclude
# ones that aren't in the list
def get_rand2(n, nums):
  s = set()
  for num in nums:
    s.add(num)
  poss_nums = []
  for num in range(n):
    if num not in s:
      poss_nums.append(num)
  if not len(poss_nums):
    return None
  rand_i = math.floor(random.random()*len(poss_nums))
  return poss_nums[rand_i]


nums = [0,1,2,3]
n = 5
print(get_rand2(n, nums))
# -> 4