# DIY Cryptocurrency - Implement a Blockchain in Python

[<< 09 Linked Lists II](https://dev.to/erikhei/modify-linked-lists-like-a-boss-in-python-565j) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/linked-lists/blockchain.py)

![bitcoin](https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fdam%2Fimageserve%2F908633080%2F960x0.jpg%3Ffit%3Dscale)
*(Image: Forbes)*

Ah, Bitcoin, everyone's favorite cryptocurrency. Bitcoin is novel in that it was able to solve the double spend problem by using a blockchain, a series of shared ledgers. Instead of having a centralized bank to hold value, blockchain is a decentralized system that allows for Byzantine Fault Tolerance, i.e., if no one person is in charge, it allows us to reach a consensus even if a couple internet trolls are trying to mess it up. 

How is the blockchain structured? Each block has a hash, and some transaction data, and a timestamp. Additionally, the block has a copy of the previous block's hash. Here is what it kind of looks like: 

![blockchain](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Bitcoin_Block_Data.svg/1920px-Bitcoin_Block_Data.svg.png)
(Source: Wikipedia)

Hmm, what does this look like? What data structure that we recently talked about on this blog? Exactly, it looks like a linked list. So today, we're going to take the Linked List class we made and turn it into a simple blockchain. With some simple modifications, you'll see how object oriented programming in Python can allow you to make some cool stuff. 

## Part 1: The OOP Struggle

First, we need to incorporate some object oriented principles in our Linked List class. Yes, I know it's a bit overcomplicated, but if we want our blockchain to be secure, we need to make some things private. This principle is called encapsulation, where some fields and methods are only accessible from inside the class. We don't want someone going in and messing around with our cryptocurrency's structure; we have to limit how they can interact with it. Updating a value would be very time consuming.

Let's begin by looking at the Node class we used for the last two lessons. I have updated to be called `Block`, since it will represent one block in the blockchain. I'm also including a couple imports that we'll use for this class.

	import datetime
	import math
	import pprint
	
	class Block:
	  def __init__(self, data):
	    self.next = None
	    self.data = data
	
	  def append(self, val):
	    end = Block(val)
	    n = self
	    while (n.next):
	      n = n.next
	    n.next = end
	    
Let's talk about a couple properties of blockchain. It's 1. immutable, meaning records are very difficult if not impossible to change, and it's 2. public. That's right, Bitcoin's blockchain is public records, and [you can go look them up right now](https://www.blockchain.com/explorer). Right now, our node's data is just stored as `data`, and anyone can access or change it using the dot notation, i.e. `my_block.data = "One Million Dollarssss"`. We don't want that. Instead, we can make the field private by adding a double underscore, changing it to `__data`, and then making a special method allowing users to read the data, so it's still public access.

	def __init__(self, data):
	    self.next = None
	    self.__data = data
		    
Next, let's make the method that allows users to read the values. In OOP, we call this a "get" method, where we simply return the value of the desired field. 

	  def get_data(self):
	    return self.__data
	    
## Part 2: Pimp My Linked List

Now that we have some security built into the class, let's add the features that make it a blockchain. First, we need to store a couple things in the data variable. We'll expand it into a dictionary that stores a couple values: the block's hash, the previous hash, the timestamp. In Bitcoin's blockchain, as you saw above, multiple transactions can be stored in one block in the form of a [Merkle Tree](https://en.wikipedia.org/wiki/Merkle_tree), but we'll keep it simple and only store one "transaction", i.e. an amount and a person. Be sure to pass in the previous hash, transactor, and amount as parameters. 

	def __init__(self, prev_hash, transactor, amount):
	self.next = None
	self.__data = {
	  "prev_hash": prev_hash,
	  "time": datetime.datetime.now().time(),
	  "transactor": transactor,
	  "amount": amount,
	  "hash": ???
	}

How do we make the block's hash? The way this works in a blockchain is that we take the previous block's hash and manipulate it using a super secret hashing algorithm. You can make yours as complicated as you want, but it could be as simple as this: 

	 def make_hash(self):
	    return self.__data["prev_hash"] + 1
    
And now we have an autoincrementing SQL database. Nice. I'm going to do something more complicated using the transaction amount times a weird power, and add the ordinal value of the last letter in the transactor's name. 

	  def make_hash(self):
	    return self.__data["prev_hash"] + int(int(self.__data["amount"])**1.5) + ord(self.__data["transactor"][-1])

Now that we have our hashing function, we have to call it in the constructor. Be sure to call it after you have defined `__data`. 

	  def __init__(self, prev_hash, transactor, amount):
	    self.next = None
	    self.__data = {
	      "prev_hash": prev_hash,
	      "time": datetime.datetime.now().time(),
	      "transactor": transactor,
	      "amount": amount,
	      "hash": ""
	    }
	    self.__data["hash"] = self.make_hash()
	    
Finally, we have to update the `append()` method. Instead of `data`, we'll take the transactor and amount as parameters. Then, we'll get the last hash before making a new block and setting its prevous hash, along with the other data. Then, attach the block to the end of the chain. 

	  def append(self, transactor, amount):
	    n = self
	    while (n.next):
	      n = n.next
	    prev_hash = n.get_data()["hash"]
	    end = Block(prev_hash, transactor, amount)
	    n.next = end


## Making the Chain Immutable

Remember how I said that blockchains are immutable, that they're very difficult to alter. The way this is done is that since each hash depends on the data stored in it (at least in my function), if the value is updated, all the hashes in the following blocks must update. This might not take very long if there are only a few blocks, but imagine we have a very long chain of blocks, and every time we update it takes O(N) time. 

We'll make a special method to update the transaction amount. I'm not sure this entirely how Bitcoin's blockchain is implemented–this is more of an assimilation. In OOP this is called a "set" method, which takes in a new value and sets the hidden data's value without the user interacting with it directly. Be sure to call the `make_hash` function to get the updated hash for the block.

	  def set_amount(self, amount):
	    self.__data["amount"] = amount
	    self.__data["hash"] = self.make_hash()
	    
But wait, we're not done. We have to update the hashes of all the following blocks. How do we do this? By way of linked list traversal, of course! You'll remember we start with a temporary pointer, and use a while loop. 

	temp = self
	while(temp.next):
	
For each block, we want to get the current block's updated hash and save it as `prev_hash`. Then, when we move to the next block, we update its hashes using the previous block's hash. I'll do this in a hidden method called `__update_hashes()`.

	def set_amount(self, amount):
		self.__data["amount"] = amount
		self.__data["hash"] = self.make_hash()
		temp = self
		while(temp.next):
		  prev_hash = temp.__data["hash"]
		  temp = temp.next
		  temp.__update_hashes(prev_hash)
      
In our `__update_hashes` method, we'll take the previous hash as a parameter and store it in `__data`, and then use the `make_hash()` function to make the current hash. 

	def __update_hashes(self, new_prev):
		self.__data["prev_hash"] = new_prev
		self.__data["hash"] = self.make_hash()
		
And that's it! We have achieved basic functionality of our blockchain.

## Testing it out

Let's build a blockchain using out `Block` method. For convenience, you can copy the following code, which I wrote to allow us to print our block chain.

	def print_chain(chain):
	  pp = pprint.PrettyPrinter(indent=4)
	  node = chain
	  pp.pprint(node.get_data())
	  while node.next:
	      node = node.next
	      pp.pprint(node.get_data())
	      
Let's make our first block. Give it a name and an amount, and remember the previous hash for the first block in the chain is always zero. 

	chain = Block(0, 'Tim', 120.00)

Next, let's append some new blocks.

	chain.append('Jamil', 200.00)
	chain.append('Carla', 123.45)
	chain.append('Sarah', 450.00)
	
	print_chain(chain)
	
You should see the following output:

	{   'amount': 120.0,
	    'hash': 1423,
	    'prev_hash': 0,
	    'time': datetime.time(0, 11, 46, 849539),
	    'transactor': 'Tim'}
	{   'amount': 200.0,
	    'hash': 4359,
	    'prev_hash': 1423,
	    'time': datetime.time(0, 11, 46, 849608),
	    'transactor': 'Jamil'}
	{   'amount': 123.45,
	    'hash': 5820,
	    'prev_hash': 4359,
	    'time': datetime.time(0, 11, 46, 849617),
	    'transactor': 'Carla'}
	{   'amount': 450.0,
	    'hash': 15469,
	    'prev_hash': 5820,
	    'time': datetime.time(0, 11, 46, 849624),
	    'transactor': 'Sarah'}
    
The hashes might be different if you used a different hashing algorithm. But the idea is that each hash is an addition onto the previous one. 

Let's try to update an amount. Setting the amount of the second person, Jamil, to something new, we should see that the hashes for all the following blocks are updated, but Tim's stay the same. 
	
	chain.next.set_amount(700)
	
	print("UPDATE:")
	print_chain(chain)
	
Output: 

	UPDATE:
	{   'amount': 120.0,
	    'hash': 1423,
	    'prev_hash': 0,
	    'time': datetime.time(0, 11, 46, 849539),
	    'transactor': 'Tim'}
	{   'amount': 700,
	    'hash': 20051,
	    'prev_hash': 1423,
	    'time': datetime.time(0, 11, 46, 849608),
	    'transactor': 'Jamil'}
	{   'amount': 123.45,
	    'hash': 21512,
	    'prev_hash': 20051,
	    'time': datetime.time(0, 11, 46, 849617),
	    'transactor': 'Carla'}
	{   'amount': 450.0,
	    'hash': 31161,
	    'prev_hash': 21512,
	    'time': datetime.time(0, 11, 46, 849624),
	    'transactor': 'Sarah'}
	    
And there you have it, you made your own cryptocurrency! Well, something like one. If you're more interested in forking the original Bitcoin code and altering it to make your own cryptocurrency, it's available [here on GitHub](https://github.com/bitcoin/bitcoin). 

That's it for this week, I hope you found this article interesting and enjoyable. Let me know in the comments what you think, or if there's any concerns--blockchain is a complicated topic, and I wrote this to my best understanding of it (special thanks to Emre Surmeli for answering all my blockchain questions!). See you next week!

[<< 09 Linked Lists II](https://dev.to/erikhei/modify-linked-lists-like-a-boss-in-python-565j) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/linked-lists/blockchain.py)

*Erik Heikkila is a Teaching Assistant at General Assembly Seattle. This blog is not associated with GA.*