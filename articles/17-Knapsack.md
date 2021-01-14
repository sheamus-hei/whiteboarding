# Help Pierre the Py Pirate Solve this Knapsack Problem!

![treasure chest](https://www.thoughtco.com/thmb/n1YuGNA1U0z4ubSMMIc_-y9QQNw=/3865x2576/filters:fill(auto,1)/buried-pirates-treasure-chest-157583040-5b5630f7c9e77c005b40d079.jpg)
*There is no love like that between a pirate and his booty. (Image: ThoughtCo)*

[<< Week 16: Find Substrings](https://dev.to/erikhei/more-python-strings-can-you-solve-this-more-difficult-string-problem-2lfj) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/misc/knapsack.py)

Remember when quarantine began, and all tech companies had to go remote? The joy we had during those first months...learning new pranks on Zoom! Students from my class will remember when I changed my inactive screen name to Pierre the Py Pirate (yes, Mac, it was me). There's nothing to break up a lecture on SQL models like a sudden "Ahoy!" from Pierre in the Zoom chat. We had a lot of fun in that class. 

This is a problem I think Pierre would enjoy, as a pirate going about his pirate-y business. Let's take a look:

	# A thief finds much more loot than he can fit in his knapsack.
	
Wait! Let me re-write this in terms Pierre would understand.

	# Pierre the Py Pirate has plundered new booty! But alas, he
	# can only fit a limited amount in the cargo hold of his ship.
	# Help him to find the most valuable combination of items 
	# assuming that any fraction of a loot item can be kept.

### 1. Setup

Let's say, for the problem, we're given two arrays: one which has the weight of each item, and one with each value. We're also given the capacity of the cargo hold. Simple enough; let's set up the method:

	def knapsack(cap, values, weights):
		pass

### 2. Strategy

Think about how you would approach this problem if you were Pierre. Let's say he has found a diamond ring, which weighs little but is worth much, and a sack of flour, which weighs a lot, but isn't worth so much. He'd want to keep the ring first, and then keep whatever flour can fill the rest of the space. So we'll start by sorting the items by their value-per-weight, and then add the most valuable items first until our capacity is reached. 

### 3. Make the Sorted List of Items

We'll start by making a new `items` list, where we'll put the sorted list of items. Then, we'll loop over the `values` list (or the `weights` list, since they're the same length). For each item, we'll store the value-per-item as `vpw`, and we'll also keep the weigth (more on this later).

	def knapsack(cap, values, weights):
	  items = []
	  for i in range(len(values)):
	    itemInfo = {
	      'vpw': values[i]/weights[i],
	      'weight': weights[i]
	    }
	    
Next, we have to add the item to the `items` list. However, we can't just tack it onto the end--this is a *sorted* list, sorted by the `vpw`. So, we'll traverse the `items` list, checking each `vpw` against the current item to see where we should put it. 

First, if there are no items in the list, we have nothing to check it against, so we'll just add it.  	 

	    if len(items) == 0:
	      items.append(itemInfo)
	     
Next, we traverse the list. We don't know the exact number of times we'll need to move, just so long as the `vpw` of our current item is less than the one in the list, we need to move closer to the end. A `while` loop would work great. 

	    else:
	      k = 0
	      while k < len(items) and items[k]['vpw'] > itemInfo['vpw']:
	      	k += 1

Okay, now our index `k` should be pointing where the new item should go. We can use the Python `insert()` method to put it there. 

	    else:
	      k = 0
	      while k < len(items) and items[k]['vpw'] > itemInfo['vpw']:
	        k += 1
	      items.insert(k, itemInfo)

### 4. Add Items from the Sorted List to the "Knapsack"

Now it's time to fill up Pierre's cargo hold. As stated earlier, we're going to go through our list of items, conveniently sorted from most value-per-weight to least, and add each one until our capacity is filled up. 

Let's make some new variables. `total` is what we're returning, the final value of Pierre's loot. Additionally, we'll make a `cap_left` variable to keep track of how much capacity is remaining after each item is added. 

	  total = 0
	  cap_left = cap

Now, we'll loop through the items. 

	  for item in items:

For each item, we'll first check to see if it fits. If so, we add its value to `total` (the value can be found by multiplying the items `weight` by the `vpw`). Don't forget to subract the weight from `cap_left`!

    if cap_left - item['weight'] >= 0 :
      total += item['weight'] * item['vpw']
      cap_left -= item['weight']

Let's say we've added a few items, and there's still room, but not enough to add the next whole item. The prompt says we can add a fraction of an item! To do this, we'll just check to see that there's some remaining capacity, and then calculate how much to add to total. There's some math involved; essentially we multiply the item's `vpw` by the remaining capacity. Then, after we've added it to the total, `cap_left` should be set to 0. 

	    elif cap_left > 0:
	      total += item['vpw'] * cap_left
	      cap_left = 0
	      
All that's left is to `return total`! Altogether: 

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
	  
### 5. Try it Out

Let's say Pierre has plundered three items, a barrel of rum, a sack of flour, and a roll of silk. He has room for 60 lbs in his ship. 

	cap = 60
	values = [60, 100, 120]
	weights = [20, 50, 30]
	
	print(knapsack(cap, values, weights))
	
	
The silk has the highest VPW at 4 gold/lb, and next is rum at 3 and flour at 2. The silk gets added first, then the rum, and finally we have 10 lbs left to fit the flour. 10 lbs of flour is valued at 20 gold, so that makes for a return total of 200 gold pieces. Yarrr!

There are many ways of solving this problem. Let me know in the comments if you think you found a better way!

[<< Week 16: Find Substrings](https://dev.to/erikhei/more-python-strings-can-you-solve-this-more-difficult-string-problem-2lfj) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/misc/knapsack.py)

*Erik Heikkila is a Teaching Assistant at General Assembly. This blog is not associated with GA.*