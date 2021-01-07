# More Python Strings: Can You Solve This *More* Difficult String Problem?

[<< Week 15: Binary Trees](https://dev.to/erikhei/binary-christmas-trees-learn-the-three-simplest-tree-traversals-in-python-41ch) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/arrays-and-strings/find_strings.py)

![Alphabet magnets](https://static.turbosquid.com/Preview/2020/03/24__10_02_23/alphabet_004_0000.jpg0DC9B5C0-7C0E-481F-81BD-F51D6005E5DALarge.jpg)
*(Image: TurboSquid.com)*

This is a problem that pops up now and again on various daily-coding-challenge platforms, like [this problem on HackerRank](https://www.hackerrank.com/challenges/find-strings/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen): given a string, find all the possible combinations of letters within that string. This is sometimes called "substrings," or if a series of lists is returned, "power sets." Let's look at one example:

	# Given a string, return a sorted list of all 
	# unique possible substrings.
	
For example, the string `'abc'` would yield the list `['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']`.

Let's start with defining our method. It takes in a string, which we'll call `word`.

	def find_substrings(word):

Next, let's think about our approach. We'll need a data structure to store all our new substrings. In the end, we'll have to return a list, but remember what it said in the prompt: *unique* substrings. So if we have the string `'aa'`, we don't want to add `'a'` twice. What data structure does this sound like? If the word *Set* comes to mind, you're right! [We've covered sets on this blog previously](https://dev.to/erikhei/more-python-practice-find-the-random-number-ft-sets-50lf), but to recap, it's a data structure that stores a series of unique values. 

To make a new set, we simply initiate the `set` object in Python.

	def find_substrings(word):
	  s = set()
	  
Now we reach the next phase of the implementation. How are we going to add each substring? Let's say we have the string `'abc'`. We can start with the first letter, `'a'`, and add it to the set. Next, we want to add the letter `'b'`, along with `'b'` concatenated to everything previously in the set, namely `'a'` to make `'ab'`.  The two rules in each iteration are:

1. Add the new letter. (e.g. `'b'`)
2. Add the new letter concatented with every previous substring (e.g. '`ab`')

However, we can simplify this into one rule. If we add an empty string to the set, we only need #2, since #1 is covered by adding the new letter to an empty string. Altogether, these are the substrings that would be added for each iteration:

|Iteration Number|Set before Addition| Letter to add| New Subsets|
|---|---|---|---|
|1 | `{ '' }` | `a` | `'a'` |
|2| `{ '', 'a' }` | `b` | `'b'` `'ab'` |
|3| `{ '', 'a', 'b', 'ab' }` | `c` | `'c'` `'ac'` `'bc'` `'abc'`|

##### Result: `{ '', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc' }`

Let's go about implementing this in code. As we established earlier, we need to start with an empty string in our set. Let's do that.

	def find_substrings(word):
	  s = set()
	  s.add('')
	  
Next, we need to define our iteration. We want to look at each letter in the string. Simple enough, we use a `for` loop. 

	  for letter in word:

Okay, so for each letter in the word, we need to loop through everything in the set and add new combos with that letter. However, if we try to change the set while we're looping through it, we'll get an error. So, we'll have to make a copy of it. 

	  for letter in word:
	    new_set = s.copy()
	    
Remember that we have to use the Python `.copy()` method, or else we'll just create a reference to the original set. This way, we have an unmodified copy to refer back to.

Next, we loop through the elements in the immutable copy. For each substring, we want to add the current letter, and then push it onto the set.

	  for letter in word:
	    new_set = s.copy()
	    for substr in new_set:
	      s.add(substr + letter)
	      
Finally, we have our substrings. We just have to do some formatting to get it how the prompt wants it. First of all, we have this extra empty string element in the set. Let's remove that. 

	  s.remove('')

Simple. Next, as you remember, we want to return a list, not a set. How do we cast something to a list? We iterate over each of its contents and wrap it in some square brackets, like so:

	  s = [letter for letter in s]
	  
We can just reassign it to `s`, since we don't need that variable for anything else. Finally, we want to sort it. Simply call the `.sort()` method on our list.

	s.sort()

And that's it, all that's left is to return `s`. Altogether:

	def find_substrings(word):
	  s = set()
	  s.add('')
	  for letter in word:
	    new_set = s.copy()
	    for substr in new_set:
	      s.add(substr + letter)
	  s.remove('')
	  s = [letter for letter in s]
	  s.sort()
	  return s
	  
### Try it Out

Call the method `find_substrings()` on the string `'abc'`, and print the result. We should get: 

`['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']`

Longer words will also work. `'abracadabra'` will give us:

`['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaab'`...

You get the idea. The point is that `'a'` only appears once, and the list is sorted alphabetically.

## Further Reading: Optimization

This was a conceptually simple solution, and the implementation of more optimal solutions won't be covered in this article. But how might we go about this?

Instead of using a set, keep the final output as a list, and only insert new strings in a sorted order. Whenever we find a new substring to add to it, we use a [binary search](https://dev.to/erikhei/algorithms-in-python-how-to-implement-binary-search-10d4) to figure out where it should be added. If the string already exists in that point, there's no need to add it again. This saves us from the O(N log N) runtime of running `sort()`.

This is one of those concepts that appears in different forms in assorted coding challenges. I hope this has added to your coding knowledge toolbox, and you'll be prepared the next time it comes up! 

[<< Week 15: Binary Trees](https://dev.to/erikhei/binary-christmas-trees-learn-the-three-simplest-tree-traversals-in-python-41ch) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/arrays-and-strings/find_strings.py)

*Erik Heikkila is a Teaching Assistant at General Assembly. This blog is not associated with GA.*

