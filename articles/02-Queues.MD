# How to Implement Stacks and Queues in Python - Part Two: Queues

[Published September 21, 2020](https://dev.to/erikhei/how-to-implement-stacks-and-queues-in-python-part-two-queues-4kme)

[<< Week 1: Stacks](https://dev.to/erikhei/how-to-implement-stacks-and-queues-in-python-part-one-stacks-32f8) | [Week 3: Miscellaneous 1 >>](https://dev.to/erikhei/whiteboarding-in-python-check-if-a-string-is-a-permutation-of-a-palindrome-2a5g)

[View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/stacks-and-queues/animal_shelter.py)

![](https://live.staticflickr.com/6032/6356491405_a06f47e327_4k.jpg)
Queue, *Aleksey Sundukov, 1986n (Source: Flickr.com)*

*For these problems, I recommend you follow along in a Repl.it.*

Welcome back to Whiteboarding with Erik, and I hope that so far these articles have been helping Data Structures seem less like Russian (unless Russian is your native language, in which case I hope they seem *more* like Russian). Having seen the above picture, you can probably guess what we'll be covering today: queues. So, let's get into it!

We'll start by looking at the stack we came up with last time. 

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


First, let me make note of one thing. In *Cracking the Coding Interview*, stacks are implemented as a Node List, not as an Array in Java. There are a few reasons for this, but since we haven't learned Linked Lists yet, I decided to keep it simple by using a list in Python.

To make a queue, we'll modify our Stack class from last week. Queues are very similar to stacks, but where stacks are LIFO–Last In First Out–queues are just the opposite, First In First Out, or FIFO. In our Stack class, we always appended new elements to the end. Then, to `pop` an element off the stack, we removed it from the end. Imagining that the start of the list is the front of the queue, we'll keep adding elements to the end, but remove them from the front instead. The `pop` method for lists in Python can take in one argument, specifying the index at which to remove an element. So, we'll simply pass in 0 as the index we want to remove. 

	removed = self.stack.pop(0)
	
The rest of our class will stay the same, apart from renaming the `stack` variable to `queue`: 

*queue.py*

	class Queue:
	    def __init__(self):
	        self.queue = []
	
	    def push(self, item):
	        self.queue.append(item)
	
	    def pop(self):
	        if len(self.queue) == 0:
	            return None
	        removed = self.queue.pop(0)
	        return removed
	        
And there you have it! Thanks for reading, be sure to like and subscribe, click the bell for notifications, and see you next week!

Okay, maybe we can try something a little more challenging.

### Queue Problem: Animal Shelter

<img src="http://www.placekitten.com/600/300" alt="place kitten">
*Finally, an excuse for me to use PlaceKitten. Maybe we can place him in a good home?*

Let's look at an example of a queue problem with more constraints.

	# An animal shelter holds dogs and cats. 
	# People must adopt either the "oldest" (based on arrival time) of any animal.
	# They can also choose a dog or cat (and will receive the oldest of that kind).
	# Create the data structures to maintain this system and implement the following methods:
	# addAnimal(), adoptAny(), adoptDog(), adoptCat()
	
Alright, given that information, we can set up the skeleton of our class. To be consistent with Python naming conventions, we'll change all the variable names from camelCase to snake_case. Also, let's add the `self` keyword as a parameter before we forget.

	class AnimalShelter:
	  __init__(self):
	    pass
	  
	  def add_animal(self):
	    pass
	  
	  def adopt_any(self):
	    pass
	    
	  def adopt_dog(self):
	    pass
	    
	  def adopt_cat(self):
	    pass
	    
As always, we'll start with the `__init__()` method. Now think, how do we want to represent each animal? How do we want to represent a queue of them? 

As for the animals, we could make an Animal class that stores information about that animal, and then create separate Dog and Cat classes which inherit those properties. However, I know object oriented programming is new to some of you, so we'll keep it simple by representing each animal with a Python dictionary, for example:

	{
		"name": "Emmy",
		"type": "dog"
	}
	
Let's think about how we want to represent the animal shelter's queue. We could use one list for both dogs and cats, but then if we wanted to call `adopt_dog()` or `adopt_cat()`, we would have to loop through the list until we found one. This would potentially put the runtime of such a method at O(N), for example, if `adopt_dog()` is called and the only dog is at the very end of the list, or if there are no dogs at all. 

Instead, we can represent split dogs and cats into two queues. Then, to adopt adopt a dog, we just have to `pop()` from the `dogs` queue, and vice versa for cats. But if we want to call `adopt_any()`, we need to pick the "oldest" animal out of either list. We can do this by keeping track of the order in which all animals were added, and add a field in each animal's dictionary to tell its order. It will look like this:

	{
		"name": "Emmy",
		"type": "dog",
		"order": 1
	}
	
When we write the `__init__()` method, we're going to initialize all the variables we need: a list representing the dogs queue, a list representing the cats queue, and the overall order, which we'll set to 0 to start. 
	
	__init__(self):
		self.dogs = []
		self.cats = []
		self.order = 0
		
Now let's add an animal to our shelter. Let's assume we know the animal's `name` and `kind` (since `type` is already a keyword in python) to start with, so these will be the method's parameters. Let's convert the `kind` to lower case for some basic mistake proofing. 
	
	def add_animal(self, name, kind):
		kind = kind.lower()

Now, let's make the `animal` dictionary using the information. We'll also need to add the `order` property, and then increment the overall order by 1. I'm going to do this before I make the animal, since I want the first animal to have an order of 1, as though it were a primary key in a SQL database. If you prefer all your indices starting at zero, you can move that line down after the `animal` object. 
		
	def add_animal(self, name, kind):
		kind = kind.lower()
		self.order += 1;
		animal = {
		  "name": name,
		  "type": kind,
		  "order": self.order
		}
		
Next, we have to decide whether we want to add it to the `cats` or `dogs` list. A simple `if` statement will do the trick. We'll print an error message in case the input doesn't match one of those options.

	  def add_animal(self, name, kind):
	    kind = kind.lower()
	    self.order += 1;
	    animal = {
	      "name": name,
	      "type": kind,
	      "order": self.order
	    }
	    if kind == "cat":
	      self.cats.append(animal)
	    elif kind == "dog":
	      self.dogs.append(animal)
	    else:
	      print("Invalid animal type entered. Animals must be cat or dog.")
	      
Okay, now let's adopt a dog. The `adopt_dog()` method simply returns the first dog in the `dogs` queue. We can pop an item off the list and return it all in one line, as shown below. We'll return `None` if the queue is empty.

	  def adopt_dog(self):
	    if len(self.dogs) == 0:
	      return None
	    else:
	      return self.dogs.pop(0)

Cool. Now let's try the same to adopt a cat. It looks about the same, but we're manipulating the `cats` queue instead. Now, I know your finger is hovering over the copy-paste button, but let's think for a moment. Every time you want to copy-paste something, there's a good chance that you could write more elegant code by creating a more general method. And that's what we'll do, we'll adapt the method we just wrote to work for both `adopt_cat` and `adopt_dog`.

We'll start by renaming the method `__adopt_animal()`. Remember last week, when I mentioned something about adding a double underscore to a variable to make it private? This concept is called "encapsulation", as one of you pointed out. Similarly, you can do the same with methods in Python to hide methods you only want to be used internally. 

The `__adopt_animal()` method will take in, addition to self, the list of animals we want to manipulate. Then, instead of performing the operations on the `dogs` list, we'll switch out those references for the new parameter, `animal_list`.

	  def __adopt_animal(self, animal_list):
	    if len(animal_list) == 0:
	      return None
	    else:
	      return animal_list.pop(0)
	      
Great, we have our more generalized function. Let's make the `adopt_dog` and `adopt_cat` methods, and in each one, we'll simply call the `__adopt_animal` method and pass it the `dogs` or `cats` list, respectively. 

	  def adopt_dog(self):
	    return self.__adopt_animal(self.dogs)
	
	  def adopt_cat(self):
	    return self.__adopt_animal(self.cats)
	    
Finally, let's look at the `adopt_any()` method. In this method, we want to return the oldest animal out of either list. We know the oldest dog is the first one in the `dogs` queue, and the same for cats in the `cats` queue, so we'll just compare them against each other. There are many ways you can write the `if` statement, but I will break it into three conditions:

1. If there are no cats, we want to adopt a dog. The `adopt_dog()` method will work even if the `dogs` list is empty. 
2. If there are dogs (and we already made sure there are cats), we want to compare them. We'll adopt a dog if the first dog is older than the first cat.
3. If there are no dogs, or the first cat is older, we want to adopt a cat.

Altogether, the method will look like this:

	  def adopt_any(self):
	    if len(self.cats) == 0:
	      return self.adopt_dog()
	    elif len(self.dogs) > 0 and self.cats[0]["order"] > self.dogs[0]["order"]:
	      return self.adopt_dog()
	    else:
	      return self.adopt_cat()
	      
I know that middle conditional is kind of long and confusing. If you think you have a better way, feel free to leave a comment!

This concludes all the methods we need to make our AnimalShelter class. We might need to reorder them so that `__adopt_animal()` is defined before it's called in `adopt_cat()` and `adopt_dog()`, and move `adopt_any()` below both of those. 

*animal_shelter.py*

	class AnimalShelter:
	  def __init__(self):
	    self.dogs = []
	    self.cats = []
	    self.order = 0
	  
	  def add_animal(self, name, kind):
	    kind = kind.lower()
	    self.order += 1;
	    animal = {
	      "name": name,
	      "type": kind,
	      "order": self.order
	    }
	    if kind == "cat":
	      self.cats.append(animal)
	    elif kind == "dog":
	      self.dogs.append(animal)
	    else:
	      print("Invalid animal type entered. Animals must be cat or dog.")
	
	  def __adopt_animal(self, animal_list):
	    if len(animal_list) == 0:
	      return None
	    else:
	      return animal_list.pop(0)
	
	  def adopt_dog(self):
	    return self.__adopt_animal(self.dogs)
	
	  def adopt_cat(self):
	    return self.__adopt_animal(self.cats)
	
	  def adopt_any(self):
	    if len(self.cats) == 0:
	      return self.adopt_dog()
	    elif len(self.dogs) > 0 and self.cats[0]["order"] > self.dogs[0]["order"]:
	      return self.adopt_dog()
	    else:
	      return self.adopt_cat()
	      
### Testing the Class

Let's test out the class we wrote. Start by making an AnimalShelter object, either at the bottom of your code or in the python shell (the right hand console on Repl.it.) I prefer minimal typing, so I'll name my AnimalShelter `a`. 

	a = AnimalShelter()
	
Next, add some animals. Remember our method takes in two arguments, the name and type. 

	a.add_animal("Pizzapie", "cat")
	a.add_animal("Emmy", "Dog")
	a.add_animal("Sushi", "Cat")
	a.add_animal("Charmander", "Dog")
	print(a.cats, a.dogs)
	
This should give us two lists, separated by cats and dogs. Notice that the `order` of each animal is auto-incrementing so that each animal has a unique order index.

Now let's adopt some of these animals. 

	a.adopt_cat()
	a.adopt_dog()
	a.adopt_any()
	print(a.cats, a.dogs)
	
The first animal to be adopted will be the cat, Pizzapie (shout-out to my students for giving me their pets' names). Next, Emmy the dog, and when we run `adopt_any()`, it will choose between Sushi and Charmander. Since Sushi was added first, she gets adopted, making Charmander the only animal left in the shelter. I hope he finds a home soon.

And that's all for this problem. If you have any questions or feedback, feel free to leave a comment. Next week, we'll take a break from classes and try a more general whiteboarding problem. If there's a particular problem you're scratching your head at, leave it in the comments, and we might just cover it sometime!

[<< Week 1: Stacks](https://dev.to/erikhei/how-to-implement-stacks-and-queues-in-python-part-one-stacks-32f8) | [Week 3: Miscellaneous 1 >>](https://dev.to/erikhei/whiteboarding-in-python-check-if-a-string-is-a-permutation-of-a-palindrome-2a5g)

*Erik Heikkila is a Teaching Assistant at General Assembly Seattle. This blog is not associated with GA.*