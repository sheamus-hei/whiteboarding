# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
# You may also use a list or array to represent a set.

# explanation: each iteration, make new items where you add that number to the end.
# then, append the new items to the list
# 0 [[], [1]]
# 1 [1], [2], [1, 2]
# 2 [1], [2], [3], [1, 2],[1,3], [2,3] ,[1,2,3]

def find_power_set(lis):
  final = [[]]
  for num in lis: # 1, 2, 3
    for j in range(len(final)):
      new_item = final[j].copy()
      new_item.append(num)
      final.append(new_item)
  return final

print(find_power_set([1,2,3]))
# -> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]