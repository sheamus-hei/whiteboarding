# (Binary) Christmas Trees! Learn the Three Simplest Tree Traversals in Python

[<< Week 14: Random Number](https://dev.to/erikhei/more-python-practice-find-the-random-number-ft-sets-50lf) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/trees-and-graphs/unival-tree.py)

![christmas tree with 1 and 0s as ornaments](https://preview.redd.it/lic4o5dvxn5y.jpg?width=640&crop=smart&auto=webp&s=c72dd64baa46657f696b4404ce74cfc29ce28e26)
*Someone on r/ProgrammingJokes thought they were really clever. (Image: Reddit)*

I've been meaning to cover the topic of binary trees on here for some time, so I thought, why not make it festive? Okay, I know it's not everyone's favorite topic. It's one of those old programming concepts that is hotly debated in the developer community. Since it's rare that you'd actually come across them in industry, it's contested whether or not they should still be fair game in an interview.

![Max Howell on Twitter: 'Google: 90% of our engineers use the software you wrote (Homebrew) but you can't invert a binary tree on a whiteboard so f off'](https://external-preview.redd.it/uJWHBA6o2sIQXno-sNs1SHHmDPV0DyQuK7ouz0gT0Xs.jpg?auto=webp&s=4c6dfa15981edace543a22bda0d039aa0a1f9cba)

We won't be inverting a binary tree today (\*phew\*), but we'll look at a couple traversal methods, and you'll find that binary trees aren't too terribly complicated to set up.

## What is a Binary Tree, Anyway?

You may remember [linked lists](https://dev.to/erikhei/what-are-linked-lists-and-how-do-i-make-one-in-python-8ea) from when we covered them in a previous article. Each list is made up of a series of nodes pointing to other nodes. But what if a node could point to more than one node? Trees are exactly that, where each parent node can have multiple children. We call it a binary tree if the max number of children is 2: a left and a right child node. 

![binary tree](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif)
*(Image: GeeksForGeeks)*

In the above example, the "root", meaning the topmost node, has a value of 1, and its children are the nodes 2 and 3, and so on. Nodes 3, 4, and 5 might be referred to as "leaves" because they have no child nodes. 

How would we go about building a tree in Python? It will look similar to our linked list Node class. We'll call it `TreeNode`.

	class TreeNode:
		pass

Next, let's define the `__init__()` method. As always, it takes in `self`, and we'll also pass in the value to be stored on the node.

	class TreeNode:
	  def __init__(self, value):

We'll set the value of the node, and then we'll define a left and right pointer, which we'll set as `None` to start.

	class TreeNode:
	  def __init__(self, value):
	    self.value = value
	    self.left = None
	    self.right = None
	    
And...that's it! What, did you think a tree would be more complicated? For a binary tree, the only difference from a linked list is that instead of `next`, we have `left` and `right`. 
 
Let's build the tree from the diagram earlier. The top node has a value of 1, and then we just keep setting its left and right nodes until we have the tree we want. 

	tree = TreeNode(1)
	tree.left = TreeNode(2)
	tree.right = TreeNode(3)
	tree.left.left = TreeNode(4)
	tree.left.right = TreeNode(5)

## Traversing the Tree

So you've built the tree, and now you're asking, "How do I see the tree I just built?" You can't just print the whole tree in one command, but we can traverse over each node. But what in what order should we print each node?

The three easiest traversals to implement are **Pre-Order**, **Post-Order**, and **In-Order**. You'll also hear the terms breadth-first and depth-first search, but the implementation of these is more complicated, so we'll cover them in a future article. So what are the three listed above? Let's look at our tree again.

![binary tree](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif)
*(Image: GeeksForGeeks)*

**Pre-Order** visits a parent node before its children. Pre-order of the above tree would result 1, 2, 4, 5, 3.

**Post-Order** visits a node's children first, and then the parent. Post-order would result in 4, 5, 2, 3, 1.

**In-Order** visits each node from left to right. In-order traversal of the the above tree would give us 4, 2, 5, 1, 3

Let's write the traversal methods for our binary tree. Start by defining the `pre_order()` method, which can go outside the `TreeNode` class. Our method takes one argument, the highest parent, a.k.a. the root node. 

	def pre_order(node):
		pass

Next, we want to check that the node exists. You could argue that we could instead check if its children exist before visiting them, but we would have to write two `if` statements, and this way we only need to write one.

	def pre_order(node):
	  if node:
	  	pass

To write the traversal is simple. Pre-order visits the parent and then each child, so we're going to "visit" the parent by printing it, and then "traverse" to the children by calling the method recursively on each child.

	# prints the parent before each child
	def pre_order(node):
	  if node:
	    print(node.value)
	    pre_order(node.left)
	    pre_order(node.right)
	    
Simple, right? You can test it out with the tree we built earlier.

	pre_order(tree)
	
And the results:

	1
	2
	4
	5
	3
	
Excellent. Next, let's do post-order. You may think that we have to write a whole new method, but actually, we just need to change one line. Instead of "visiting" the node and then "traversing" the children, we just "traverse" the children first, and then "visit" the parent node. What do I mean by this? Simply move the print statement to the last line! Remember to change the name of all your function calls to `post_order()`. 

	# prints children and then parent
	def post_order(node):
	  if node:
	    post_order(node.left)
	    post_order(node.right)
	    print(node.value)
	    
Printing the result should give us the following: 

	4
	5
	2
	3
	1
	
Where each child node is visited before its parent. 

Last, we need to write the In-Order traversal. How do you traverse the left node, and then visit the parent, and then traverse the right? Again, we just move the print statement! 

	# prints left child, parent, then right child
	def in_order(node):
	  if node:
	    in_order(node.left)
	    print(node.value)
	    in_order(node.right)
	    
Now if we print the tree, the nodes are printed "in order."

	4
	2
	5
	1
	3
	
And there you have it, the three simplest ways to traverse a binary tree. Have a happy holiday, however you celebrate (socially distanced of course). I hope this helped you learn more about the binary trees!

[<< Week 14: Random Number](https://dev.to/erikhei/more-python-practice-find-the-random-number-ft-sets-50lf) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/trees-and-graphs/unival-tree.py)

*Erik Heikkila is a Teaching Assistant at General Assembly. This blog is not associated with GA.*