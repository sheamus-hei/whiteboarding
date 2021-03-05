# Linked Lists
 
 *Erik Heikkila @ General Assembly 2021*
 
## Overview
 
 1. What are they? 
 2. Why use them?
 3. How to make them
 4. Traverse them
 5. Modify them (insert and delete)
 
## 1. So What Are They?

* A list of nodes connected by links
* Each node has at least two things:
	1. Some kind of stored data
	2. A pointer to the next node

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/408px-Singly-linked-list.svg.png)

*(Image: Wikipedia)*

* Can be Singly- or Doubly-Linked

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)

*(Image: Wikipedia)*


### Pros and Cons of Singly- vs Doubly- Linked Lists
| | Singly | Doubly |
|---|----|---|
|Pros| simple manipulation| more ways to traverse|
|Cons| can only traverse one direction| more links to keep track of makes for more complicated manipulation|
 
* For the vast majority of interview questions you will be asked about **singly-**linked lists. But it's good to ask.

## 2. But Why Though?

* "Why not use a JS array or Python list?" 
* These are actually **Dynamic Arrays**!
* Traditional Arrays have a **fixed size** that you must declare at initializiation.
* "But what if I want to add things to my array?" You need to make a new array of size N + 1 and move everything in there

e.g. `[1, 2, 3]` -> `[0, 0, 0, 0]` -> `[1, 2, 3, 0]`

* Dynamic Arrays (used for JS and Python lists) are just a traditional array that automatically to increase the size if you go over the limit.

### Comparison Between Linked Lists and Arrays
* In general, Linked Lists are better for *updating* and Arrays/Dynamic Arrays are better for *accessing* data. 

Look at [this table](https://en.wikipedia.org/wiki/Dynamic_array#Performance) from Wikipedia:

<table class="wikitable">
<caption>Comparison of list data structures
</caption>
<tbody><tr>
<th>
</th>
<th><a href="/wiki/Linked_list" title="Linked list">Linked list</a>
</th>
<th><a href="/wiki/Array_data_structure" title="Array data structure">Array</a>
</th>
<th><a class="mw-selflink selflink">Dynamic array</a>
</th>
<th><a href="/wiki/Self-balancing_binary_search_tree" title="Self-balancing binary search tree">Balanced tree</a>
</th>
<th><a href="/w/index.php?title=Random_access_list&amp;action=edit&amp;redlink=1" class="new" title="Random access list (page does not exist)">Random <span class="nowrap">access list</span></a>
</th>
<th><a href="/wiki/Hashed_array_tree" title="Hashed array tree">Hashed array tree</a>
</th></tr>
<tr>
<td>Indexing
</td>
<td style="background:#ffdddd">Θ(<i>n</i>)
</td>
<td style="background:#ddffdd">Θ(1)
</td>
<td style="background:#ddffdd">Θ(1)
</td>
<td style="background:#ffffdd">Θ(log n)
</td>
<td style="background:#ffffdd">Θ(log n)<sup id="cite_ref-okasakiComparison_11-0" class="reference"><a href="#cite_note-okasakiComparison-11">&#91;11&#93;</a></sup>
</td>
<td style="background:#ddffdd">Θ(1)
</td></tr>
<tr>
<td><span class="nowrap">Insert/delete</span> at beginning
</td>
<td style="background:#ddffdd">Θ(1)
</td>
<td data-sort-value="" style="background: #ececec; color: #2C2C2C; vertical-align: middle; text-align: center;" class="table-na">N/A
</td>
<td style="background:#ffdddd">Θ(<i>n</i>)
</td>
<td style="background:#ffffdd">Θ(log n)
</td>
<td style="background:#ddffdd">Θ(1)
</td>
<td style="background:#ffdddd">Θ(<i>n</i>)
</td></tr>
<tr>
<td><span class="nowrap">Insert/delete</span> at end
</td>
<td style="background:#ddffdd">Θ(1) when last <span class="nowrap">element is known</span>;<br />Θ(<i>n</i>) when last <span class="nowrap">element is unknown</span>
</td>
<td data-sort-value="" style="background: #ececec; color: #2C2C2C; vertical-align: middle; text-align: center;" class="table-na">N/A
</td>
<td style="background:#ddffdd">Θ(1) <a href="/wiki/Amortized_analysis" title="Amortized analysis">amortized</a>
</td>
<td style="background:#ffffdd">Θ(log <i>n</i>)
</td>
<td data-sort-value="" style="background: #ececec; color: #2C2C2C; vertical-align: middle; text-align: center;" class="table-na">N/A <sup id="cite_ref-okasakiComparison_11-1" class="reference"><a href="#cite_note-okasakiComparison-11">&#91;11&#93;</a></sup>
</td>
<td style="background:#ddffdd">Θ(1) <a href="/wiki/Amortized_analysis" title="Amortized analysis">amortized</a>
</td></tr>
<tr>
<td><span class="nowrap">Insert/delete</span> in middle
</td>
<td style="background:#ffffdd">search time + <span class="nowrap">Θ(1)</span><sup id="cite_ref-12" class="reference"><a href="#cite_note-12">&#91;12&#93;</a></sup><sup id="cite_ref-13" class="reference"><a href="#cite_note-13">&#91;13&#93;</a></sup>
</td>
<td data-sort-value="" style="background: #ececec; color: #2C2C2C; vertical-align: middle; text-align: center;" class="table-na">N/A
</td>
<td style="background:#ffdddd">Θ(<i>n</i>)
</td>
<td style="background:#ffffdd">Θ(log <i>n</i>)
</td>
<td data-sort-value="" style="background: #ececec; color: #2C2C2C; vertical-align: middle; text-align: center;" class="table-na">N/A <sup id="cite_ref-okasakiComparison_11-2" class="reference"><a href="#cite_note-okasakiComparison-11">&#91;11&#93;</a></sup>
</td>
<td style="background:#ffdddd">Θ(<i>n</i>)
</td></tr>
<tr>
<td><span class="nowrap">Wasted space</span> (average)
</td>
<td style="background:#ffdddd">Θ(<i>n</i>)
</td>
<td style="background:#ddffdd">0
</td>
<td style="background:#ffdddd">Θ(<i>n</i>)<sup id="cite_ref-14" class="reference"><a href="#cite_note-14">&#91;14&#93;</a></sup>
</td>
<td style="background:#ffdddd">Θ(<i>n</i>)
</td>
<td style="background:#ffdddd">Θ(<i>n</i>)
</td>
<td style="background:#ffffdd">Θ(<span class="nowrap">&#8730;<span style="border-top:1px solid; padding:0 0.1em;"><i>n</i></span></span>)
</td></tr></tbody></table>


## 3. How to Make Them

* For a singly-linked list, you just need a `Node` class with  `data`and `next`. 

		class Node:
			def __init__(self, data):
				self.data = data
				self.next = None
				
* You can just keep track of the first node, or you can wrap them in a `LinkedList` class. 

		class LinkedList:
		    def __init__(self):
		        self.head = None
		        self.tail = None
		        self.size = 0
		
		    # returns length of the list
		    def __len__(self):
		        return self.size
		
		    def __str__(self):
		        if self.size == 0:
		            return '[]'
		
		        current = self.head
		        result = str(current) # what we return once we've concantenated all the nodes to it
		        while current.next:
		            result += f' -> {str(current.next)}'
		            current = current.next
		        return f'[{result}]'
        
   (Source: GA Gitbook)
   
## 4. Traverse It

* To access any node, we need to start at the head and traverse the list for worst case O(N) runtime (if we need to reach the last node). 
* Use recursion or a while loop!

		head = Node(1)
		head.next = Node(2)
		head.next.next = Node(3)
		
		print(head.data)
		node = head
		while node.next:
		    node = node.next
		    print(node.data)   
			
			
* Recursion:

		def traversal(node):
		  if node:
		    print(node.data)
		    traversal(node.next)
	    
* Notice how we check `if node`. This is our recursive base case! 

## 5. Modify It 
	
* Usually instead of checking `if node` or `while node`, we check `if node.next` or `while node.next`
* Why? In a singly-linked list, we can only go forwards. This means we can only modify links after the current node. 
* Remember links are like "balloons tied together". If you cut one link, all the nodes after it "float away"

### Example: Remove Duplicates

	from collections import defaultdict
	def remove_dups(front):
	  counted = defaultdict(bool)
	  temp = front
	  counted[temp.data] = True
	  while (temp.next):
	    # check the value of next Node
	    if (counted[temp.next.data]):
	      #if found in dictionary, remove it
	      temp.next = temp.next.next
	    else:
	      counted[temp.next.data] = True
	      temp = temp.next