# Back to Basics: More Strings in Python

[<< Week 9: Blockchain](https://dev.to/erikhei/diy-cryptocurrency-implement-a-blockchain-in-python-4a9m) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/arrays-and-strings/urlify.py)

![website address bar](https://www.howtogeek.com/wp-content/uploads/2018/06/shutterstock_1006988770.png)
*(Image: HowtoGeek.com)*

Last week we [implemented a blockchain](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/arrays-and-strings/urlify.py), which was quite intensive, so this week I opted to give you a break with a simple string problem. It's good practice, right? Let's take a look.

	# Write a method to replace all spaces in a string with '%20'. 
	# Ignore any additional white space at the beginning or end of the string.
	
If you've been on the internet, which I imagine you have, you may have noticed that URLs never have spaces in them. If you try to type a URL in your browser and include a space, you might notice it converts it to an escape character: '%20'. Try typing "http://google.com/ /" in Chrome, and you'll see it converts it to "http://google.com/%20/". Not that that page goes anywhere, but you get the point.

For this challenge, we're going to write a method to do what your browser just did, i.e. take a url as a string and return the encoded form with spaces replaced by '%20'. Let's start by defining our method which takes in a string `s`. 

	def urlify(s):
		pass
		
Next, let's take a look at the fine print: *ignore any additional white space at the beginning or end of the string.* Let's take care of this right away by using the Python `strip()` method to remove any leading or trailing whitespace on our string. 

	def urlify(s):
		s = s.strip()
		
Let's think about addressing these spaces. We could loop through the string and look at each character, checking if it's a space, and if so, replace it. However, there's an easier way to do this. Python has some built in methods to split a string based on a given character. Then, we can join them back together with "%20" replacing the spaces. 

Start by calling the `split()` method. We can call this after our `.strip(). The method takes one argument, the divider character, which in our case is " ", a single space.

	def urlify(s):
	  s = s.strip().split(" ")
  
This should give us a list of strings. For example, if the string was "Hello my name is Erik", now `s` is a list containing ["Hello", "my", "name", "is", "Erik"]. 

Now we just have to join the list items together. The `.join()` method is a little strange; you call it on the string you want to put in between the words, and pass in the list as an argument. So, if our replacement string is "%20", we call `.join()` after it (I'm just wrapping it with parentheses), and pass it `s`, which is now a list. We could redefine this variable to `s`, but I'm just going to return it. 

	def urlify(s):
	  s = s.strip().split(" ")
	  return ("%20").join(s)
	  
And that's it! To recap: 

1. Strip whitespace.
2. Split on the space character.
3. Join with "%20" in between each item.

## Test it out

Pass our `urlify` method a string containing some spaces. It should return a string with those spaces replaced by the URL escape character.

	print(urlify("My name is Erik "))
	# -> My%20name%20is%20Erik
	
That's it for this week; hopefully we gave your brain a rest after all those linked lists. Don't forget about them for too long, as next week we'll be tackling the dreadnaught–binary trees. See you then!

[<< Week 9: Blockchain](https://dev.to/erikhei/diy-cryptocurrency-implement-a-blockchain-in-python-4a9m) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/arrays-and-strings/urlify.py)

*Erik Heikkila is a Teaching Assistant at General Assembly Seattle. This blog is not associated with GA.*
