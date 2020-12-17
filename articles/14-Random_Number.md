#More Python Practice: Find the Random Number (ft. Sets!)

[<< Week 13: Diving Board](https://dev.to/erikhei/dive-into-python-with-this-diving-board-problem-ft-recursion-453p) | [View Solution on Github](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/arrays-and-strings/random_num.py) 

![Wall of lava lamps](https://images.fastcompany.net/image/upload/w_596,c_limit,q_auto:best,f_auto/wp-cms/uploads/sites/4/2017/08/i-2-this-security-firms-office-design-adds-to-the-strength-of-its-encryption.gif)

*Cloudflare in San Francisco uses [lava lamps](https://www.fastcompany.com/90137157/the-hardest-working-office-design-in-america-encrypts-your-data-with-lava-lamps) as a random number generator to encrypt requests (Source: Fast Company)*

Random numbers, the spice of life. Or, at least in the coding world, they are. The [Bored API](https://www.boredapi.com/) uses random numbers to find an activity to alleviate your boredom, and games like Minecraft use them to spawn random terrain (check out my simple 2D Javascript Minecraft spin-off [here](https://erik-hei.github.io/frogcraft/)). And there are more practical uses, like encryption at CloudFlare, which uses a [wall of lava lamps](https://www.fastcompany.com/90137157/the-hardest-working-office-design-in-america-encrypts-your-data-with-lava-lamps) as a random number generator to encrypt web requests. 


So let's talk about using random numbers in Python. Here is a sample interview question.

	# Given an integer n and a list of integers, 
	# write a function that randomly generates a number 
	# from 0 to n-1 that isn't in the list.

There are two things we'll need if we're going to generate a random integer. One is the Python `random` library, and we'll also need the `math` library to round down our random number to an integer. 

	import random
	import math
	
Next, as always, we define our method. It takes in a number and a list of integers, which we'll call `nums`. 

	def get_rand(n, nums):
		pass

## Solution 1: Reroll

Let's talk strategy. The first one we'll discuss is a "galaxy brain" sort of idea that perhaps first comes to mind: find a random number in the given range, and then if it's in the list, simply run the random number generator again until we find one that's valid.

We'll start by getting a random number between 0 and n. The `random` object has a method called `random()` which returns a random (decimal) number between 0 and 1. To get a numbet between 0 and n, we multiply it by n, and then we round down using `math.floor()`


	  rand_num = math.floor(random.random() * n)


You might start by getting the random number, but there's something else we can use to make the (pretty terrible) runtime a bit better. Let's look at something used in many programming languages called a set.

*Set* - A data type that stores unique values in no particular order.

![cloud of numbers](https://dev-to-uploads.s3.amazonaws.com/i/rzmfwazi2ugmx71l5mi9.png)
*A visualization of the Set datatype.*

I like to think of sets as a cloud: a bunch of numbers floating around, but there's no order to them. What's important is that no number appears twice. If you try to add 3 to a set, and it's already in there, it won't get added again. What's useful for us is that checking to see if the set contains a certain number takes constant O(1) time. This is better than the O(N) time we'd get if we had to loop through a list every time.

How do we implement a set in Python? Start by calling the set class with its constructor, `set()`. 


	  s = set()
	  
Next, we add the numbers from the list into the set. 

	for num in nums:
	    s.add(num)
	    
Now we check to see if the random number we made is in the set. If not, we want to find a new random number. This can be achieved with a `while` loop that runs if the random number is in the set. For fun, you can put a print statement to see how many times the method has to find a new number before it finds one that is valid. 

	  while rand_num in s:
	    print("reroll")
	    rand_num = math.floor(random.random()*n)
	    
And finally, we return the resulting random number once the `while` loop has been exited. Altogether:

	def get_rand(n, nums):
	  rand_num = math.floor(random.random()*n)
	  s = set()
	  for num in nums:
	    s.add(num)
	  while rand_num in s:
	    print("reroll")
	    rand_num = math.floor(random.random()*n)
	  return rand_num
	  
If we try it out by printing `get_rand(5, [0, 1, 2, 3])`, we should get 4, which is the only number left that is less than 5, and that isn't in the list. 

As I mentioned earlier, the runtime for this solution is not terribly efficient. Potentially, the algorithm could keep picking random numbers into eternity if it doesn't find the right one--which is exactly what happens if there *are* no numbers that meet the criteria. Why don't you try printing the result of `get_rand(5, [0, 1, 2, 3, 4])`, where the list contains all the numbers that are less than 5. Does it look like this?

	reroll
	reroll
	reroll	
	reroll
	reroll
	reroll
	reroll
	...

The algorithm keeps rerolling to eternity since there are no possible numbers to choose from. Let's think of a different solution that will both address this edge case and eliminate infinite runtime.

## Solution 2: List of Possible Numbers

Sometimes, we approach these programming questions as though we're solving a math program, and we forget: we're *developers*. We *build things*. So one approach is to always ask, "Can I build the thing I need to solve this problem?"

Imagine instead of having to check each time if our random number was in the list, we already had of list of valid numbers to choose from. Then, we would just pick a random number in the list. This would also solve our edge case, because we would know that this list of possible numbers is empty, we should return None.

The first part of our method will remain the same: we take the numbers from the `nums` list and put them in a set. Then, we want to make an empty list that will contain all the possible numbers to choose from.

	def get_rand2(n, nums):
	  s = set()
	  for num in nums:
	    s.add(num)
	  poss_nums = []

How do we find the valid numbers? We simply loop through every integer from 0 to `n`, and if it's not in the set, we add it to the list. 

	  for num in range(n):
	    if num not in s:
	      poss_nums.append(num)
	      
If we were to run our call from earlier, `get_rand(5, [0, 1, 2, 3])`, we would get a list of `poss_nums` containing only the number 4. 

Next, we check for our edge case. Simply check if the list is empty, and if so, return `None`. 

	  if not len(poss_nums):
	    return None

What's left? To pick our random number, of course! Using the `random.random()` function, we multiply it by the length of the list to  pick a random index, and then we'll return the number at that index. 

	  rand_i = math.floor(random.random()*len(poss_nums))
	  return poss_nums[rand_i]
	  
That's it! The method looks like this in total:

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
		  
Now, if we try running `get_rand(5, [0, 1, 2, 3, 4])` and print the result, we should get None because there are no numbers that meet the criteria. Hooray! No more infinite loops. 

That's all for this week. If you like this content, please let me know in the comments what you would like to see next!

[<< Week 13: Diving Board](https://dev.to/erikhei/dive-into-python-with-this-diving-board-problem-ft-recursion-453p) | [View Solution on Github](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/arrays-and-strings/random_num.py) 

*Erik Heikkila is a Teaching Assistant at General Assembly. This blog is not associated with GA.*
