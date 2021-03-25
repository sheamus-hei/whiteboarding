# Sum of Three, Sum of Four, and Beyond? In Python!

[<< #21 Tree Practice](https://dev.to/erikhei/binary-tree-practice-in-python-mirror-tree-1hl) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/arrays-and-strings/sum_of_k.py)

![cat asleep on computer](https://images.squarespace-cdn.com/content/v1/58e534c52e69cfd83dc862d9/1491615962126-ZTBJOQQM2RXAENSEBEJI/ke17ZwdGBToddI8pDm48kCPztTQZpDiZMOuuCfUxiyx7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1UYlQ-m0oNUh_9buvyC-f1CSdhG_dNlqULB2ZTz-ses64A-QPhXXvNcU0N8wN7BGx0g/cat-sleeping-on-the-job?format=1500w)
*Actual pic of me after trying to solve this problem (Image: ThatCatBlog.com)*

Today's problem has stumped many a programmer. A colleague of mine and I sat down with "Sum of Three", talked it out, and after more than an hour, finally finished a solution that was by no means elegant or optimal. I was joking with him that next we should try "Sum of Four", which I had totally made up. Turns out, [it's real](https://leetcode.com/problems/4sum/). After another long whiteboarding session, we came up with...a bunch of ideas and no solution. 

We were so focused on finding an elegant solution that we missed being able to solve the problem at all. But here's an obvious solution: brute force. Brute force may be simple, and it certainly isn't optimal, but it gets the job done. And when you have no other solution, it helps to have at least one way to solve it. 

![It ain't much, but it's honest work.](https://i.kym-cdn.com/entries/icons/original/000/028/021/work.jpg)
*(Image: KnowYourMeme)*

Today, we're going to look at "Sum of Three" and "Sum of Four", and solve them using brute force. Then, you'll see how we can expand the brute force solution using recursion to allow for "Sum of K", which will work for 3, 4, or any amount of numbers we want to sum up. You'll see that having a brute force solution might not be scalable, but you can still build some powerful things. 

Let's get started with the simpler problem, "Sum of Three". Here is the prompt: 

	# Given an array nums of n integers and a target,
	# are there elements a, b, c in nums 
	# such that a + b + c = target?
	
	# Example:
	
	# Input: 
	# nums = [-1,0,1,2,-1,-4]
	# target = 0
	
	# Output: [[-1,-1,2],[-1,0,1]]
	
	# Notice that the solution set must not contain duplicate triplets.

Were given a list of numbers, and we want to find every three numbers in the list that sum to zero, or whichever number is specified at the target. How would you go about solving this?

## 1. Approach

The brute force solution will involve iteration. Imagine we look at each number, and check it against every other number, and then check those two numbers against every other other number. What does this sound like? If you said a triple nested `for` loop, you're right (I'm sure there must also be a recursive way to do this part...let me know in the comments if you found it!). 

But theres one other caveat, as listed in the prompt: `Notice that the solution set must not contain duplicate triplets`. How will we account for this? If you've been following this blog, you're probably thinking of using a set (more on this [here](https://dev.to/erikhei/more-python-practice-find-the-random-number-ft-sets-50lf)). And yep, that's what we will be using. We'll codify each working triplet into a string and put it in the set to make sure we haven't included it already. 

## 2. Setup

We're ready to start writing this bad boy. Our method `sum_of_three` will take in two arguments: the list `nums` and the `target`. 

	def sum_of_three(nums, target):

Next, we need to check for an edge case. What if `nums` has less than 3 numbers in it? Then we can't find a triplet. In this case, we'll return an empty list. 

	def sum_of_three(nums, target):
	  if len(nums) < 3:
	    return []
	    
Finally, we need to initialize some variables that we'll be using. Firstly, the `output` list which will contain lists of triplets. We'll also start one of those triplet lists and call it `current`. Once we populate `current` with a working triplet, we can append it to `output`. 

	  output = []
	  current = []
	  
And, as discussed earlier, we'll need to make a set. Additionally, we'll want to sort the list to make sure we don't add the same triplet to the set, just in a different order (for instance, only one of `[1, -2, 1]` and `[1, 1, -2]` should be added). 

	  checked = set()
	  nums.sort()
	  
## 3. Iteration

We're ready to start our `for` loops. We're making three of them, and the most important part to consider is our indices' upper and lower bounds. 

For the first loop, we'll start with the first number in the list and go until the 3rd from the last spot. Why? We need two additional numbers to check this with, and once we get to the 2nd or last index, there aren't enough numbers behind it to make a triplet. 

	  for i in range(len(nums) - 2):

As a review, `range(start, end)` accepts two arguments: a start (inclusive) and an end (exclusive). If the start argument is missing, it's assumed to be 0. 

Okay, what will we do inside this first `for` loop? Here's the agenda:

1. Add the first number to `current`. 
2. Subtract that number from the sum. 
3. Check it with the other numbers.
4. Undo steps 1 and 2 so we can move on to the next number. 

Let's write these in code. The first one is easy, simply `append` the number at index `i` to current. 

	    current.append(nums[i])
	    
The next step is also pretty simple. You can subtract from the `target`, but I prefer making a new variable that makes it clear that we're changing it, called `working_target`. 

	    working_target = target - nums[i]
	    
Step 3 is more complicated. "Check it with the other numbers" is my shorthand for doing the nested `for` loops. I'll comment it out for now.

Step 4 is simple. Remove the last element from current with `current.pop()`, and to move the target back, well, we don't need to do anything because it's going to be re-instantiated each iteration. Altogether, our loop looks like this so far: 

	  for i in range(len(nums) - 2):
	    current.append(nums[i])
	    working_target = target - nums[i]
	    # do some for loops
	    current.pop()

Great, we're ready to move onto loop #2. 

What are our indices? We start at the index after `i` and go until the second-to-last spot in `nums`. 

	    for j in range(i + 1, len(nums) - 1):
	    
Next, we follow our steps 1-4 again. That is, we append the number at `j` to `current`, subtract it from `working_target`, leave space for the next loop, and then undo steps 1 and 2. 

	    for j in range(i + 1, len(nums) - 1):
	      working_target -= nums[j]
	      current.append(nums[j])
	      # do another for loop
	      current.pop()
	      working_target += nums[j]

Finally, we can write our innermost loop. The indices should be familiar by now, we start at `j + 1` and go until the last index. 

	      for k in range(j + 1, len(nums)):

We can append the number at `k` to `current`, but when we subtract from the `working_total`, now we want to check if it equals zero. If the numbers all sum to the target, then `target - a - b - c = 0` (if you remember back to algebra class). 

	      for k in range(j + 1, len(nums)):
	        current.append(nums[k])
	        if working_target - nums[k] == 0:

What goes in the `if` statement? Now it's time to use our set to determine if we've checked this triplet already. 

We can't put lists into a set, so we have to codify our triplet into a string. The following code will make a string with &s in between the numbers, for example, `[1, 1, -2]` will get turned into `1&1&-2`. You can use any character you want to deliniate the numbers, but you need something so `1, 11` isn't confused with `11, 1`. 

	          # make code to put in duplicate set
	          code = str(current[0])
	          for n in range(1, len(current)):
	            code += "&" + str(current[n])

Now we can check to see if the code is in the set. If not, we can add it to the set and add `current` to our final `output`. Remember to add a copy of `current`, and not just the reference. Otherwise, our triplet could change after we add it to `output`!	     
	          if code not in checked:
	            output.append(current.copy())
	            checked.add(code)
	            
Lastly, we pop the third number off of current. Altogether, the final `for` loop:

	      for k in range(j + 1, len(nums)):
	        current.append(nums[k])
	        if working_target - nums[k] == 0:
	          # make code to put in duplicate set
	          code = str(current[0])
	          for n in range(1, len(current)):
	            code += "&" + str(current[n])
	          if code not in checked:
	            output.append(current.copy())
	            checked.add(code)
	        current.pop()

## 4. Wrapping up Sum of Three

All that's left is to return our `output` list. Then, we're done! Here is the full method; be sure that your indentation matches exactly after all those `for` loops: 

	def sum_of_three(nums, target):
	  if len(nums) < 3:
	    return []
	  output = []
	  current = []
	  checked = set()
	  nums.sort()
	  for i in range(len(nums) - 2):
	    current.append(nums[i])
	    working_target = target - nums[i]
	    for j in range(i + 1, len(nums) - 1):
	      working_target -= nums[j]
	      current.append(nums[j])
	      for k in range(j + 1, len(nums)):
	        current.append(nums[k])
	        if working_target - nums[k] == 0:
	          # make code to put in duplicate set
	          code = str(current[0])
	          for n in range(1, len(current)):
	            code += "&" + str(current[n])
	          if code not in checked:
	            output.append(current.copy())
	            checked.add(code)
	        current.pop()
	      current.pop()
	      working_target += nums[j]
	    current.pop()
	    working_target += nums[i]
	  return output
	  
Here is some sample driver code to test the method:

	nums = [-1,0,1,2,-1,-4]
	target = 0
	print(sum_of_three(nums, target))
	
This will give us the final output of `[[-1,-1,2],[-1,0,1]]`. Notice how there are no duplicate triplets, even though there are two `-1`s to make the second triplet. 

## 5. Step Up Complexity: Sum of Four

You were feeling pretty good, just finished Sum of Three. But can you next solve...sum of *four*?

Although it sounds more complex, conceptually, we can use the same brute force method. I know that our runtime will go from the terrible O(N<sup>3</sup>) to the even worse O(N<sup>4</sup>), but like I said earlier. It will still \*run\*. 

How will we achieve this? We can simply adjust our code from `sum_of_three` by *adding another loop*. Each loops starts at the previous index + 1 and ends progressively closer to the end of the list. Here is what they will look like: 

	 for i in range(len(nums) - 3):
	    for j in range(i + 1, len(nums) - 2):
	      for k in range(j + 1, len(nums) - 1):
	        for m in range(k + 1, len(nums)):
	        
In each loop, we'll follow the same steps as before: appending to `current`, subtracting from the target, checking some stuff, and then undoing the previous actions. I'll save you some scrolling and post the method in full: 

	def sum_of_four(nums, target):
	  if len(nums) < 4:
	    return []
	  output = []
	  current = []
	  nums.sort()
	  checked = set()
	  for i in range(len(nums) - 3):
	    working_target = target - nums[i]
	    current.append(nums[i])
	    for j in range(i + 1, len(nums) - 2):
	      working_target -= nums[j]
	      current.append(nums[j])
	      for k in range(j + 1, len(nums) - 1):
	        working_target -= nums[k]
	        current.append(nums[k])
	        for m in range(k + 1, len(nums)):
	          current.append(nums[m])
	          if working_target - nums[m] == 0:
	            # make code to put in duplicate set
	            code = str(current[0])
	            for n in range(1, len(current)):
	              code += "&" + str(current[n])
	            if code not in checked:
	              output.append(current.copy())
	              checked.add(code)
	          current.pop()
	        current.pop()
	        working_target += nums[k]
	      current.pop()
	      working_target += nums[j]
	    current.pop()
	  return output
	  
This exactly matches our method for "Sum of Three", just with an extra loop. We can run the following driver code: 

	nums = [1,0,-1,0,-2,2, 0]
	target = 0
	print(sum_of_four(nums, target))
	
And our result is `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`. It works!

## 6. Sum of Five...and Beyond?

You wrote "Sum of Three" and "Sum of Four"; you're feeling pretty confident. What if I told you next you need to solve...Sum of Five? 

No problem, you say. Just add another `for` loop. But you might have noticed something. This looks a little repetitive: 

    for j in range(i + 1, len(nums) - 2):
      working_target -= nums[j]
      current.append(nums[j])
      for k in range(j + 1, len(nums) - 1):
        working_target -= nums[k]
        current.append(nums[k])
        for m in range(k + 1, len(nums)):
          current.append(nums[m])
          
And you're right. When we have repetitive code, a good practice is to write a method for it. So what if we wrote a recursive method to run each `for` loop? Then, we could tell it how many numbers we want to sum together, and it will know how many nested loops to construct. 

We'll set up the method exactly we have as before, although this time, we take in an argument `k` of how many numbers (triplet, quadruplet, etc.) to sum. 

	def sum_of_k(nums, target, k):
	  if len(nums) < k:
	    return []
	  output = []
	  current = []
	  nums.sort()
	  checked = set()

Next, we'll make a recursive method called `sum_helper()` that accepts...pretty much every variable we have so far. Additionally, we need to know the previous index (for when we start the loop at `i + 1`), which starts at 0. This method will alter the arrays, so we just need to call it and then afterwards, return `output`. 

	  sum_helper(nums, target, k, output, checked, current, 0)
	  return output
	  
## 7. Iteration in the Recursive Method

Let's think about our approach for the recursive helper method. Each time, we're going to be subtracting from `k`. After all, "Sum of Four" is just "Sum of Three" with an extra number attached. 

Our recursive method will need a base case. If `k` is zero, we don't have to do anything. In this case, we'll simply `return` out of the function. 

	  if k == 0:
	    return
    
If `k` is greater than zero, we want to loop through `nums`. We'll start at the index `prev` and go until the end of the list - k + 1 (we get this by looking at the pattern in our previous solutions). 

	  for i in range(prev, len(nums) - k + 1):
	  
What's next? Look at our list: we append the current number to `current`. 

	    current.append(nums[i])
	    
You might think the next step is to subtract that number from the target, but we need to check something first. This `for` loop needs to be universal for every iteration of `k`, and we need to account for if this is the innermost loop. 

If this is the case, we need to check if the target minus the number is zero. Then we do exactly what we did before (you could probably copy paste with minimal edits) by adding to the set and if unique, add to the output. 

    if k == 1 and target - nums[i] == 0:
      # make code to put in duplicate set
      code = str(current[0])
      for n in range(1, len(current)):
        code += "&" + str(current[n])
      if code not in checked:
        output.append(current.copy())
        checked.add(code)
        
Now we can subtract from the working target and write our recursive case. But wait, we can do this all in one step! Here is the recursive call: 

    sum_helper(nums, target - nums[i], k - 1, output, checked, current, i + 1)
    
 So `target` moves, `k` goes down 1, and the current index + 1 becomes the previous index `prev`. 
 
Finally, we have to undo our addition to `current`:

    current.pop()
    
And that's it! Together, here are our methods: 

	def sum_of_k(nums, target, k):
	  if len(nums) < k:
	    return []
	  output = []
	  current = []
	  nums.sort()
	  checked = set()
	  sum_helper(nums, target, k, output, checked, current, 0)
	  return output
	
	def sum_helper(nums, target, k, output, checked, current, prev):
	  if k == 0:
	    return
	  for i in range(prev, len(nums) - k + 1):
	    current.append(nums[i])
	    if k == 1 and target - nums[i] == 0:
	      # make code to put in duplicate set
	      code = str(current[0])
	      for n in range(1, len(current)):
	        code += "&" + str(current[n])
	      if code not in checked:
	        output.append(current.copy())
	        checked.add(code)
	    sum_helper(nums, target - nums[i], k - 1, output, checked, current, i + 1)
	    current.pop()
	    
Our method is still pretty unwieldy, but we don't have to adjust it for every changing `k`. The following driver code will work whether `k` is 3, 4, or beyond!

	nums = [-1,0,1,2,-1,-4, -2]
	target = 0
	k = 4
	print(sum_of_k(nums, target, k))
	# -> [[-2, -1, 1, 2], [-1, -1, 0, 2]]
	
Again, this is a brute force solution. The run time will be O(N<sup>k</sup>), which is pretty bad if `k` is large. This problem could probably be solved more elegantly with linear algebra, so if some of you are particularly knowledgeable on that front and come up with something, let me know in the comments!

[<< #21 Tree Practice](https://dev.to/erikhei/binary-tree-practice-in-python-mirror-tree-1hl) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/arrays-and-strings/sum_of_k.py)

*Erik Heikkila is a Teaching Assistant at General Assembly. This blog is not associated with GA.*
	