# Dive into Python with this Diving Board Problem (ft. Recursion)!

[<< Week 12: Robot](https://dev.to/erikhei/robot-vacuum-in-python-bring-him-home-2gig) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/add_to_k.py)

![corgi diving into a pool](https://www.mandatory.com/assets/uploads/gallery/poolside-gifs/giphy-3.gif)
*Like a pro. (Image: Mandatory.com)*

I'm going to say one word: Recursion. What is your initial reaction? Fear? Excitement? Back in my CS days at uni, they made sure to take caution introducing this subject: *"It's so unintuitive!"*

In all honesty, though, recursion is just another way to solve iterative problems. We got our `for` loops, for 10 times do X. But in recursion, *X* is to call the same method again. And instead of calling it 10 times, we call it until the conditions are met. What are the conditions? That's for us to determine. Let's look at this sample interview question.

	# A diving board must be built to a certain length,
	# made up only of the given pieces of wood
	
	# Given a list of numbers (the lengths of wood)
	# and a number k, return whether any two numbers 
	# from the list add up to k.
	
	# For example, given [10, 15, 3, 7] and k of 17, return 
	# True, since 10 + 7 is 17.
	
First, let's take a step back and think how we might solve this iteratively. A "brute force" solution, if you will. We'll simply create a nested `for` loop where we check every single number against every other number in the list to see if they add to `k`. 

Start with a method `add_to_k()` that takes in two parameters, our `numbers` list, and the sum `k`. 

	def add_to_k(numbers, k):
	  pass
	  
Our first `for` loop will run up through the end of the list minus 1, since by the time we get to the last element, there's nothing behind it to compare it with.

	def add_to_k(numbers, k):
	  for i in range(len(numbers) - 1):
	    ...
	    
We'll keep track of the first number we find and call it `current`. Next, we want to look at all the numbers in the list behind it. This can be achieved with the nested `for` loop as shown.

	def add_to_k(numbers, k):
	  for i in range(len(numbers) - 1):
	    current = numbers[i]
	    for j in range(i + 1, len(numbers)):
			...
			
Finally, if the sum of the two numbers is equal to `k`, we return True. If we loop through the entire list without finding a match, we return False. Altogether:

	def add_to_k(numbers, k):
	  for i in range(len(numbers) - 1):
	    current = numbers[i]
	    for j in range(i + 1, len(numbers)):
	      # print("checking", current, "+", numbers[j])
	      if current + numbers[j] == k:
	        return True
	  return False  

Let's try running the solution. 

	num_list = [10, 15, 3, 7]
	k = 10
	
	print(add_to_k(num_list, k))
	# -> True

Great. This solution does the trick, but how would we go about solving it recursively? 

## Writing the Recursive Solution

The method will start the same, taking in the same `numbers` and `k` parameters as before.

	def add_to_k_recursive(numbers, k):
	  pass
	  
Now, we need to determine our base case(s). With recursion, the best thing to ask is, "What is the simplest case?" Put on your lazy engineer hat; if you had to solve this problem looking at a bunch of different lists, which one would you want to solve? Perhaps a list that only has one item, in which case, the answer must always be false. This is our primary base case. I'm making the length less than 2, since an empty list would also fall into this category.

	def add_to_k_recursive(numbers, k):
	  if (len(numbers) < 2):
	    return False
	    
What's next? We have one more base case to write. If a list must be at least 2 long, the easiest case would be...if the list were only 2 long! Then we would simply add the two numbers and see if they equal `k`. In the case that we don't know the length of the list, let's default to checking the first and last number. 

	def add_to_k_recursive(numbers, k):
	  if (len(numbers) < 2):
	    return False
	  elif numbers[0] + numbers[-1] == k:
	    return True

Now all we have to do is make our recursive case, i.e., the one where we call our method again. 

Let's think about it. Our list is `[10, 15, 3, 7]`, and we're looking for numbers that sum to 10. Obviously, the length is longer than 2, so we skip the first `if` statement. In the `elif`, we see that the first and last numbers, 10 and 7, add to 17, which is not 10. So now what?

We'll have to call `add_to_k_recursive()` on a smaller list so that the first and last numbers are different. There are two lists we can check:

1. Everything but the first value.
2. Everything but the last value.

These are, in python:

	numbers[1:]
	numbers[:-1]

So, we'll call our method twice, once for each of the two smaller lists. What do we return? Remember that in Python, `or` will return the first True value. So, we return one method call or the other.

	def add_to_k_recursive(numbers, k):
	  if (len(numbers) < 2):
	    return False
	  elif numbers[0] + numbers[-1] == k:
	    return True
	  else:
	    return add_to_k_recursive(numbers[:-1], k) or add_to_k_recursive(numbers[1:], k)
	    
## Testing it Out

Running the same code as before should give us the same output of True.

	num_list = [10, 15, 3, 7]
	k = 10
	
	print(add_to_k_recursive(num_list, k))
	
However, let's look at what's going on under the hood.

We start with the list `[10, 15, 3, 7]`. As stated before, the first and last numbers don't add to 10. So, we call the function again on the smaller lists, `[10, 15, 3]` and `[15, 3, 7]`.

Each of those lists will get broken down again, so the second list will get split into `[15, 3]` and `[3, 7]`, the last one returning True. So, True gets returned up the chain of command through the initial instance of our method.

I hope this helped clear up your understanding of recursion. We didn't make the run time any better, since we still have to look at every number about two times, or O(N<sup>2</sup>) complexity. However, you might look at this solution and find it more elegant. Regardless, recursion is a good trick to have in your bag, especially if you see the words "check all possible combinations" looming in an interview question. 

[<< Week 12: Robot](https://dev.to/erikhei/robot-vacuum-in-python-bring-him-home-2gig) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/add_to_k.py)

*Erik Heikkila is a Teaching Assistant at General Assembly. This blog is not associated with GA.*