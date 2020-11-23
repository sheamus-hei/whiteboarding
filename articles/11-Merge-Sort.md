# Merge Sort: When You're Too Much of a Nerd to Use `.sort()`

[<< Week 10: Urlify](https://dev.to/erikhei/back-to-basics-more-strings-in-python-3cn1) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/search-and-sort/merge_sort.py)

It's the age old question. *"I have a list of things and I want to sort them. What do?"* 

![bunch of legos](https://ichef.bbci.co.uk/news/800/cpsprodpb/92F3/production/_114391673_gettyimages-1158923430.jpg)
*(Image: BBC)*

Well, clearly, the most intuitive answer is to take the list, divide it in half, and in half and in half until you have a bunch of lists 1 length long, and then put each pair back together in the right order, and then put the little sorted pairs together in bigger sorted pairs, and then again until you have a full list, but sorted. Is that what you were thinking? 

![merge sort diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Merge_sort_algorithm_diagram.svg/600px-Merge_sort_algorithm_diagram.svg.png)
*Looks something like this. (Source: Wikipedia)*

Okay, so maybe it's not the most intuitive solution, but I'll spare you the tedious hand holding of walking through inferior search algorithms like bubble sort and bogo sort (\*shudder\*) before explaining merge sort. What you need to know is that merge sort has a pretty good runtime compared to other algorithms, which, as you may have guessed from the whole "split in half" thing, is O(N log N). 

Let's get started. Make the `merge_sort()`, which takes in a list. We'll call it `nums` for our purposes, but this same method would work for a list of any sortable types, such as strings. 

	def merge_sort(nums):
		pass
		
The first step is to divide the list in half. Use integer division to make sure we get a whole number index (in case the list is odd). Then we'll make two smaller lists, `left` and `right`, using python's handy sub-list notation. Wait, what if the list is 0 or 1 long? Then we can't split it in half. This is why we wrap our entire method in an if statement, ensuring it only operates if the list is greater than 1.

	def merge_sort(nums): 
	  if len(nums) >1: 
	    mid = len(nums)//2
	    left = nums[:mid] 
	    right = nums[mid:]
	    
What do we do next? Simple! Sort the two halves by calling `merge_sort()` on them. 

	def merge_sort(nums): 
	  if len(nums) >1: 
	    mid = len(nums)//2
	    left = nums[:mid] 
	    right = nums[mid:]
	    merge_sort(left) 
	    merge_sort(right) 
	    
But wait, we're not done. So far, we've split the list into halves repeatedly until we have a bunch of little lists length one. For example, if we had the list `[4, 2, 1, 3]`, it would get split into `[4, 2]` and `[1, 3]`, and then into `[4]`, `[2]`, `[1]`, and `[3]`, lists each of length 1. 

What's next? I'll give you a hint, it's in the name of the method...rhymes with blurge....right! We merge the halves together. 

Things get a little tricky here. We need to keep track of a few indices, which we'll call `i`, `j`, and `k`. Here is what they represent:

* `i` is an index in the `left` list.
* `j` is an index in the `right` list.
* `k` is the index in the original list, `nums` where we want to put each number when we're done.

To start, we'll make all of them zero.

	i = j = k = 0
	
Next, we're going to traverse both the left and right lists, comparing each item. We only need to go through once because `left` and `right` are already sorted. We just need to merge them. 

If the number in `left` is smaller, we put it back in `nums` at spot `k`, and advance our left index `j`. If the number in `right` is smaller (or equal), we put it in `nums` instead, and advance our right index, `j`. Finally, we advance `k` now that we have added a new number to `nums`. 
	
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            nums[k] = left[i] 
            i+=1
        else: 
            nums[k] = right[j] 
            j+=1
        k+=1
        
There's one more thing we need to do. We said `while i < len(left) and j < len(right)`, meaning as soon as one of those conditions is met, the loop will break. So let's say we reached the end of `left`, but we still have more indices to go in `right`? We just have to make another while loop that accounts for this, looping through the rest of `right` and adding its numbers into the `nums` list. We do the same for any numbers left in `left` (ha, left, get it? I'll stop now). 

    while j < len(right): 
        nums[k] = right[j] 
        j+=1
        k+=1
        
    while i < len(left): 
        nums[k] = left[i] 
        i+=1
        k+=1
      
That's it! To recap the merge, we started with `[4]`, `[2]`, `[1]`, and `[3]`. These get merged to `[2, 4]` and `[1, 3]`, and then finally they come together to make `[1, 2, 3, 4]`. 

Here is the full code. Notice that the bulk of the method lies within that first `if` statement.

	def merge_sort(nums): 
	  if len(nums) > 1: 
	    mid = len(nums)//2
	    left = nums[:mid] 
	    right = nums[mid:]
	    merge_sort(left) 
	    merge_sort(right) 
	
	    i = j = k = 0
	      
	    while i < len(left) and j < len(right): 
	        if left[i] < right[j]: 
	            nums[k] = left[i] 
	            i+=1
	        else: 
	            nums[k] = right[j] 
	            j+=1
	        k+=1
	
	    while i < len(left): 
	        nums[k] = left[i] 
	        i+=1
	        k+=1
	      
	    while j < len(right): 
	        nums[k] = right[j] 
	        j+=1
	        k+=1
	        
## Testing it out

Let's sort some numbers. Make a list of numbers, and call `merge_sort()` on them. Notice how we print the result *after* the method call, since it alters the original list `nums` instead of returning anything.

	nums = [5, 2, 3, 6, 84, 9, 8]
	merge_sort(nums)
	print(nums)
	
This should give you the sorted list, `[2, 3, 5, 6, 8, 9, 84]`. As mentioned before, this will also work with strings. Giving the list `['banana', 'apple', 'grape', 'orange']` will sort alphabetically to `['apple', 'banana', 'grape', 'orange']`.

I hope this gave you some clarity on how merge sort works. Python's `.sort()` method is similar to merge sort and is another "divide and conquer" algorithm, and has about the same time complexity. So, there's not really a reason you would have to implement merge sort...unless you're asked to do so on an technical interview. I hope this helped to prepare you for that!

[<< Week 10: Urlify](https://dev.to/erikhei/back-to-basics-more-strings-in-python-3cn1) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/search-and-sort/merge_sort.py)

*Erik Heikkila is a Teaching Assistant at General Assembly. This blog is not associated with GA.*
	