# What are Linked Lists and How Do I Make One in Python?

[<< Week 7: Misc 03](https://dev.to/erikhei/that-really-tricky-ispandigital-problem-but-in-python-59i) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/linked-lists/remove-duplicates.py)

![chain links](./img/chain.jpg)

First, I have an announcement that I'm going to start making my articles shorter and more easier to digest. Hopefully they'll make for more light coffee reading than full-on Thanksgiving meals.

This week, we're talking about linked lists. Maybe you have heard of them? Maybe you saw them mentioned in a lesson on data structures and thought "that sounds too finicky, why wouldn't we just use an array?" Well, there are some advantages to linked lists over an array or list. They may seem complicated at first, but don't worry, I'm going to hold your hand and walk you through it. 

Now that you have the image of us holding hands, you have a good idea of the structure of linked lists: a bunch of single nodes held together by links, i.e. references to other nodes. There are two kinds, singly and doubly linked lists:

![single and double linked list](https://miro.medium.com/max/1230/1*5wRMqVjLatOGX88VrZgacA.jpeg)
*(Image: Medium.com)*

In singly linked lists, each node has one arrow pointing forwards, and doubly linked lists have an additional arrow pointing backwards. In general, though, most of the questions you encounter will assume singly-linked lists. Why? They're simpler to implement, and although you don't have the luxury of traversing the list backwards, let me tell you, arrows pointing in one direction are enough for your brain to keep track of. 

Let's try implementing a linked list in Python. You may think to start with `class Linked_list`, and then make a bunch of nodes inside of it, but it's simpler than that. Imagine we're making a chain of paper clips: we get a bunch of paper clips and string them together.

![string of paperclips](https://media.istockphoto.com/photos/colored-paper-clip-chain-on-white-background-picture-id172486630)

What makes the chain is the individual paperclips plus the fact that you strung them together. Instead of making a `Linked_list` class, we'll simply make a `Node` class and allow for individual nodes to be linked together.

	class Node:
	
Next, as always when making a class in Python, we make the `__init__` method. This is the method that initializes all the fields i.e. variables in the class whenever a new `Node` object is made. We'll take in a variable called `data` which is the value we want to store on the node. We also have to define the forward link, which is traditionally called `next`. To start, the node isn't connected to anything, so we set it to `None`. 

	class Node:
		def __init__(self, data):
			self.data = data
			self.next = None

That's about all we need. We could leave it at that, but *Cracking the Coding Interview* also implements a method called `appendToTail()` which makes a new node and appends it to the end of the list, traversing the list so we don't have to do that manually. Let's take a look at it.

Start by defining it within the `Node` class. It will take in the value that we want to give the new node, and for Python, the `self` keyword. 

	class Node:
		def __init__(self, data):
			self.data = data
			self.next = None
			
		def append(self, val):
			pass

The first thing we do is make a new node with the given value. We'll call it `end`. 

	  def append(self, val):
	    end = Node(val)
	    
Next, we make a pointer. It might sound technical, but essentially, we're making a reference to the head of our list. This is because we want to traverse the list without reassigning anything in the list. Thus, we make a reference to the first node, `self`, and save it with the variable `n`. 

	  def append(self, val):
	    end = Node(val)
	    n = self
	    
Finally, we traverse the list. How do we do this? We only want to move to the next node if there *is* a next node, and if not, we know we're at the end. We'll use a simple while loop to traverse to the next-to-last node. 

	  def append(self, val):
	    end = Node(val)
	    n = self
	    while (n.next):
	      n = n.next

Finally, we're pointing at that last node, which has no next. We simply take `end`, which is our new node, and set `n.next` to be `end`.
  
	  def append(self, val):
	    end = Node(val)
	    n = self
	    while (n.next):
	      n = n.next
	    n.next = end
	    
That's it! Here is our full class:

*list_node.py*

	class Node:
	  def __init__(self, data):
	    self.next = None
	    self.data = data
	
	  def append(self, val):
	    end = Node(val)
	    n = self
	    while (n.next):
	      n = n.next
	    n.next = end

### Testing our Linked List

Let's try it out. Start by making a new `Node` object; I'm calling it `ll` (two lowercase Ls standing for Linked List) and giving it a value of 1. 

	ll = Node(1)
	
Now, since we added that sweet `append()` method, we can call it to add new nodes to our list. 

	ll.append(2)
	ll.append(3)
	
How do we see what our list looks like? Theoretically, it should look kind of like this:

#### [1] --> [2] --> [3] 

But there's no way to just print that. We have to traverse the list and print each value. But you remember how to do a list traversal, right? We just did one. To recap:

1. Make a variable to point to the head
2. While there is a next node, move to that node.

Then, we'll just print the `data` at each node. We start with step #1 by making a new variable and assigning it to the head of the list.

	node = ll
	
Next, we print the first node. Why don't we start the while loop? The while loop will only iterate twice, because only two of the nodes have a `next`–the last node does not. In computer science, we call this a "fencepost problem", where you need to do something X times, plus one. You can think of a fence, where you have a post, then some fence, then a post, and a fence and so on. 

![wooden fence](https://www.logproducts.com/wp-content/uploads/2020/03/Hand-carved-wood-fence-Sawtooth-Wood-Products-Sun-Valley-Idaho-scaled-2000x800_c.jpg)
*(Image: Sawtooth Wood Products)*

But you can't leave that last piece of fence hanging. You need a post on the end. So, you can either add another post on the end, or, as is more common in CS, make the first post and then build the rest of the fence. This is what we'll do.

First, we print the first node, and then we run the while loop to print out each following node.

	node = ll
	print(node.data)
	while node.next:
	    node = node.next
	    print(node.data)
	    
Running this for our previous list, we should get:

	1
	2
	3

Printed to the console. And there we go! Our linked list works. 

That's it for this week! Thanks for reading, and next week we'll look at a linked list problem, and we'll learn more about how to manipulate our linked lists, since it works a little differently than regular Python lists. As always, drop me a comment if you have any questions, or want to see more!

    
[<< Week 7: Misc 03](https://dev.to/erikhei/that-really-tricky-ispandigital-problem-but-in-python-59i) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/linked-lists/remove-duplicates.py) 

*Erik Heikkila is a Teaching Assistant at General Assembly Seattle. This blog is not associated with GA.*