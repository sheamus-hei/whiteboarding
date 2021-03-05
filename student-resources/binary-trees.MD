# Binary Trees
 
 *Erik Heikkila @ General Assembly 2021*
 
## Overview
 
 1. What are they? 
 2. Why use them?
 3. How to make them
 4. Traverse them

 
## 1. What are Binary Trees?

*  A graph (next lesson) where each node has up to 2 children. 


 ![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Binary_tree.svg/300px-Binary_tree.svg.png)
 
 *(Image: Wikipedia)*

* Has a *root* and *leaves* 
* Above, the root is 2 and leaves are the lower 2, 5, 11, and 4.

* **Binary Search Trees** are binary trees where the values of all the left nodes are less than the values of all the right nodes. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/360px-Binary_search_tree.svg.png)

*(Image: Wikipedia)*

## 2. Why Use?

* The depth of a balanced tree is 2<sup>N</sup> nodes deep, so worst case access of is O(log N), significantly better than O(N)
* If the tree is not balanced, worse case is still O(N) because we basically have a Linked List

## 3. Traversal

	#       1
	#     /   \
	#    2     3
	#   / \    
	#  4   5

* IMPORTANT: Interviewers will want to know: **Breadth-First Search** or **Depth-First Search**
* **BFS** starts at root and looks progressively at rows of children. In the above tree: 1, 2, 3, 4, 5
* **DFS** travels down to each leaf. There are three kinds:

	1. **Pre-Order** visits a parent node before its children. Pre-order of the above tree would result 1, 2, 4, 5, 3.
	
	2. **Post-Order** visits a node's children first, and then the parent. Post-order would result in 4, 5, 2, 3, 1.
	
	3. **In-Order** visits each node from left to right. In-order traversal of the the above tree would give us 4, 2, 5, 1, 3

### DFS Example 

* The following is for pre-order traversal:

		def traversal(node):
		  if node:
		    print(node.value)
		    traversal(node.left)
		    traversal(node.right)
	    
* For in- and post-order, simply move the print statement!

### BFS Example

This is more complicated. Maybe look at my [blog post](https://dev.to/erikhei/more-python-binary-trees-what-is-breadth-vs-depth-first-search-25la).

### Traversal Practice

* "Write a function that counts the total number of nodes in the tree."

		def count_nodes(node):
		  if not node:
		    return 0
		  else:
		    return 1 + count_nodes(node.left) + count_nodes(node.right)

* "Write a function that finds the minimum value in a tree."

		import sys
		def find_min(node):
		  if not node:
		    return sys.maxsize
		  else:
		    left_min = min(node.value, find_min(node.left))
		    right_min = min(node.value, find_min(node.right))
		    return min(left_min, right_min)


