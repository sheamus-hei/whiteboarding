# PROMPT
# A thief finds much more loot than his bag can fit. Help him to find the most valuable combination of items assuming that any fraction of a loot item can be put into his bag.
# The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
# Input Format. 
# 	capacity: number of n items and the capacity w of a knapsack. (n, w)
# 	every i-th line for n lines:
# 		values: value of item (v-i)
# 		weights: weight of item (w-i)
# 	The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value and the weight of 𝑖-th item, respectively.
# 	Constraints. 
# 		1 ≤ 𝑛 ≤ 10^3
# 		0 ≤ 𝑊 ≤ 2·10^6
# 		0 ≤ 𝑣𝑖 ≤ 2·10^6
# 		0 < 𝑤𝑖 ≤ 2·10^6 for all 1 ≤ 𝑖 ≤ 𝑛.
# 		All the numbers are integers.
# 	Output Format. 
# 		Output the maximum value of fractions of items that fit into the knapsack.  The absolute value of the difference between the answer of your program and the optimal value should be at most 10^(-3).  To ensure this, output your answer with at least four digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
# SAMPLE
# 	input:   			3, 50 (n, W)
# 	 							60, 20 (v1, w1) value per weight = 3
# 									100, 50 (v2, w2) value per weight = 2
# 									120, 30 (v3, w3) value per weight = 4
# 	output:				180.0000
# 	explanation:		To achieve the value of 180, 120 + 120(20 / 30) = 200
# 	input:   			1, 10
# 	output:				500, 30
# 	explanation:		Here, we just take one third of the only available item. 


def knapsack(cap, values, weights):
  items = []
  for i in range(len(values)):
    itemInfo = {
      'vpw': values[i]/weights[i],
      'weight': weights[i]
    }
    if len(items) == 0:
      items.append(itemInfo)
    else:
      k = 0
      while k < len(items) and items[k]['vpw'] > itemInfo['vpw']:
        k += 1
      items.insert(k, itemInfo)
  total = 0
  cap_left = cap
  for item in items:
    if cap_left - item['weight'] >= 0 :
      total += item['weight'] * item['vpw']
      cap_left -= item['weight']
    elif cap_left > 0:
      total += item['vpw'] * cap_left
      cap_left = 0
  return total


cap = 50
values = [60, 100, 120]
weights = [20, 50, 30]


print(knapsack(cap, values, weights))