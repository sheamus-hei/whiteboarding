# How to Implement Stacks and Queues in Python - Part One: Stacks

Published September 14, 2020 

[<< Week 0: Introduction](https://dev.to/erikhei/how-to-learn-data-structures-and-algorithms-when-you-re-fresh-out-of-your-bootcamp-2bob) | [Week 2: Queues >>](https://dev.to/erikhei/how-to-implement-stacks-and-queues-in-python-part-two-queues-4kme)

[View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/stacks-and-queues/simple_stack.py)



*I highly recommend you follow along in a Repl.it of your own. Of course, on a whiteboard during an interview, you won't have syntax highlighting, but when learning for the first time, I think it helps to make sense of things!*

Happy Monday, folks! We're kicking off the series on Data Structures and Algorithms with-- what a surprise-- data structures! Stacks and Queues to be exact. As with most whiteboarding problems, maybe you'll never have to use them in industry, but they're a good way to show you know how to implement classes--AKA "make a thing that does what you tell it to do." 

The concept for stacks and queues are relatively simple. Stacks are just like a stack of plates: you always remove the one on top, the last one placed. You'll hear the term LIFO - Last In First Out. Queues are just the opposite, the first item in is the first to be removed. Imagine a queue at Starbucks, the first customer to order is always the first to be served their coffee (unless they ordered drip coffee and got served right away? Um...ignore that). 

<img src="https://insideoutstyleblog.com/wp-content/uploads/2017/09/broad-museum-stack-of-plates.jpg" height=350 alt="a stack of plates"><img src="http://img.koreatimes.co.kr/upload/newsV2/images/21-01(45).jpg/dims/resize/740/optimize" height=350 alt="a line at starbucks"><br>
*IRL Stack and Queue.*

### Making a Stack in Python
So let's look at a simplified example of what you may be asked on a technical interview. If you're following along at home, time to tab out and open up a Repl.it. 

	# Implement a stack that has the following methods:
	# 1. push(item), which pushes an element onto the stack
	# 2. pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
	# Each method should run in constant time.
	
It starts with the word "implement" meaning they want a class. If you're not used to working with classes, they're essentially a blueprint to an object. When we initiate a new object with the class `Stack`, it will have all the properties and methods we defined when making the class. 

We'll start by defining the class, and then add the `__init__` method. Additionally, we'll add the empty methods `pop()` and `push()`. The keyword `pass` is just so that Python won't get upset that we have an empty method. 

	class Stack:
		def __init__():
			pass
		
		def pop():
			pass
		
		def push():
			pass
			
Neat, now we have a `Stack` class. Let's define the `__init__` method, which will determine all the properties of the stack upon initialization. I.E., every time a new stack is born, we're going to give it some things. Any ideas?

A stack is essentially a list (remember, arrays are called "lists" in Python) with some special properties - you can only add or remove the most recent element. So we'll represent it as a list, which I'll call `stack`. To define a property of a class in Python, we'll use the `self` keyword. To access this keyword, it must also be passed in as an argument to the method.

	def __init__(self):
		self.stack = []
		
Alright, let's move on to the `push()` method. This will also take in `self` as an argument so we can access that `stack` variable we just defined. Additionally, it'll take in an `item`, the one we want to add to the top of the stack. 

	def push(self, item):
		pass
		
To add and take away items from the stack, we'll imagine the end of the list as the top. This makes things easy in Python, since we can use the `.append()` method to add an item to the end of a list, like so:

	def push(self, item):
		self.stack.append(item)
		
The `pop()` method will be similar. Python has a `.pop()` method for lists which removes the final element in the list. Convenient! The method returns the element that was removed, so we'll save it in a local variable called `removed` and return it. 

	def pop(self):
		removed = self.stack.pop()
		return removed
		
*BUT WAIT!* We have a problem. What if there are no items left to remove in the stack? Luckily, the prompt gave us some fine print to remind of us this potential pitfall: 

	# If there are no elements in the stack, then it should throw an error or return null.
	
So all we need to do is add a conditional statement to check for this edge case. To do so, before we run `.pop` on the list, we'll just add an if statement to check if the stack is empty. The only null type in Python is `None`, so we'll return that in this case. 

	def pop(self):
		if len(self.stack) == 0:
			return None
		removed = self.stack.pop()
		return removed
		
And that's it! To recap:

*stack.py*

	class Stack:
		def __init__(self):
			self.stack = []
			
		def push(self, item):
			self.stack.append(item)
		
		def pop(self):
			if len(self.stack) == 0:
				return None
			removed = self.stack.pop()
			return removed
		
Another thing to note is that our solution follows the constraint that all methods run in constant time, O(1). This means they all run in the same time regardless of the length of the stack. If we had needed to loop the list, for example, the time complexity would be O(N), N being the length of the list. But we didn't, so we're good.

### Testing our Stack

You may have been following along in Repl.it so far, and good job. But you'll notice if you run the program, nothing happens. 

![magicarp nothing happened](https://i.imgur.com/6IgOPnm.png)

Like I said, classes are like blueprints to an object. We made the blueprint, so let's test it out by making an object. You can either do this from the Python shell (the terminal output on Repl.it) or at the bottom of your stack.py file. For simplicity's sake, I'm naming my stack `s`. 

	>>> s = Stack()

Now, let's test out that beautiful `push()` method we wrote by adding a few numbers to our stack. 

	>>> s.push(1)
	>>> s.push(2)
	>>> s.push(3)
	
If we print out `s.stack`, we should get `[1, 2, 3]`. Great. So let's try the `pop()` method. 

	>>> s.pop()

Now, if we print `s.stack`, we should get `[1, 2]`. Notice how only the last item was removed, and the value of 3 was returned. But what happens if we keep removing elements? We can test to see if our method returns `None` by running the same command a few more times, and then printing the return value. 

	>>> s.pop()
	>>> s.pop()
	>>> print(s.pop())
	
And there you have it, a stack implemented in Python. You officially learned your first data structure.

### Bonus: Integrating a max() method

The sample question I found was apparently asked on an Amazon interview, and it asked for an additional method: 

	# 3. max(), which returns the maximum value in the stack currently. 
	# If there are no elements in the stack, then it should throw an error or return null.
	
We'll have to change a couple things about our Stack class to make this work. Let's start with the `__init__`. Let's add a variable `max` to keep track of the max value in the stack. The prompt suggested it return a null value if the stack is empty, so we'll initialize it to `None`. 
	
	def __init__(self):
		self.stack = []
		self.max = None
		
Cool, now let's update  the `push()` method. There are two cases we'll need to check for:

1. If this is the first item to be added to the stack. In this case, `max` is currently `None`, and we need to initialize it to the first value being added. 
2. If there is already a value for `max`, we need to compare it with the item being added and update accordingly. 

In both cases, we'll be setting the new `max` value to the item being added. Thus, a one-line `or` statement will do the trick. 

	def push(self, item):
	    self.stack.append(item)
	    if len(self.stack) == 1 or item > self.max:
	    	self.max = item
	    	
Next, we'll look at `pop()`. Again, there are two cases we need to check for:

1. If the item being removed is the last in the stack. Now that the stack is empty, we should set `max` to `None`. 
2. If the item being removed is equal to the max value, we need to loop through the list and find the new value. 

The first case is simple. After we call `.pop()` on the list, we check to see if the length is now zero. 

	if len(self.stack) == 0:
		self.max = None
	      
For the second case, we'll use a `for` loop. We'll start by setting the `max` to a value we know already exists in the stack: the first value. Then, we'll loop through the list and check each value against it, updating it accordingly. 

	elif removed == self.max:
      self.max = self.stack[0]
      for value in self.stack:
        if value > self.max:
          self.max = value
          
Finally, we'll return the value we removed from the stack. Altogether, the method will look like this: 

	def pop(self):
		if len(self.stack) == 0:
    		return None
    	removed = self.stack.pop()
    	if len(self.stack) == 0:
      		self.max = None
    	elif removed == self.max:
      		self.max = self.stack[0]
      		for value in self.stack:
        		if value > self.max:
          			self.max = value
    	return removed
    	
Finally, let's implement the `max()` method as advertized. The purpose of the method is just to return the `max` value we defined. But here's the thing, in Python we can just access that value outside of our class definition by calling `s.max`. Why do we need to write a whole method just to return it? 

This is another holdover from object oriented programming in Java. Traditionally, it's best practice to keep all our variables private. If you were building say, a radio, you wouldn't want users being able to mess with the wires inside, only the knobs and buttons on the outside. In Java, you would initialize that `max` field with the keyword `private`. Then, you would make a method called `max` or `get_max()` that returns that value--otherwise the only way to access it. 

There is a way to make variables private in Python, simply define it with a double underscore ("dunder" for you nerds) like so: `__max`. It's up to you whether you want to do this; on an interview, the best practice would be to ask your interviewer what they want. The fact that you're asking means you're bright and insightful, and then you can give them what they want. 

To recap:

*stack.py*

	class Stack:
	  def __init__(self):
	    self.stack = []
	    self.max = None
	
	  def pop(self):
	    if len(self.stack) == 0:
	      return None
	    removed = self.stack.pop()
	    if len(self.stack) == 0:
	      self.max = None
	    elif removed == self.max:
	      self.max = self.stack[0]
	      for value in self.stack:
	        if value > self.max:
	          self.max = value
	    return removed
	
	  def push(self, item):
	    self.stack.append(item)
	    if len(self.stack) == 1 or item > self.max:
	      self.max = item
	
	  def get_max(self):
	    return self.max
	    
And there you have it! You can test out adding and removing elements to check that the max updates properly. 

	>>> s = Stack()
	>>> s.push(1)
	>>> s.push(2)
	>>> s.push(3)
	>>> s.max
	3
	>>> s.pop()
	3
	>>> s.max
	2
	
Well, folks, that's it for this week. I hope this gave you some insight into how defining classes works in Python, as well as understanding a few data structures. We'll return next week to implement queues. Thanks for reading, and see you then!

[<< Week 0: Introduction](https://dev.to/erikhei/how-to-learn-data-structures-and-algorithms-when-you-re-fresh-out-of-your-bootcamp-2bob) | [Week 2: Queues >>](https://dev.to/erikhei/how-to-implement-stacks-and-queues-in-python-part-two-queues-4kme)

*Erik Heikkila is a Teaching Assistant at General Assembly Seattle. This blog is not associated with GA.*