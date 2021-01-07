# WIP!! SOLUTION NOT WORKING
# given an infinite number of quarters, dimes, and nickels, write a code to calculate the number of ways of representing n cents

def coin_helper(total, denoms, i):
  coin = denoms[i]
  print("coin:", coin, "index", i, "total", total)
  if (i == (len(denoms) - 1)):
    remaining = total - coin
    print(remaining)
    if remaining == 0:
      print("Match found")
      return 1
    else:
      return 0
  ways = 0
  # for (let amount = 0; amount <= total; amount += coin)
  for j in range(total//coin):
    print("J", j)
    ways += coin_helper(total - j * coin, denoms, i + 1)
  return ways

def find_coin_combos(n, denoms):
  return coin_helper(n, denoms, 0)

# 25 => 
# 1 quarters
# 2 dimes 1 nickel
# 2 dimes 5 pennies
# 1 dime 3 nickels
# 1 dime 2 nickels 5 pennies
# 1 dime 1 nickels 10 pennies
# 1 dime 15 pennies
# 5 nickels
# 4 nickels 5 pennies
# 3 nickels 10 pennies
# 2 nickels 15 pennies
# 1 nickel 20 pennies
# 25 pennies

n = 5
denoms = [1, 5, 10, 25]
print(find_coin_combos(n, denoms))
