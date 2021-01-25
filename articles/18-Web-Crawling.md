# Web Crawling in Python: Dive Into Beautiful Soup

[< Week 17: Knapsack](https://dev.to/erikhei/help-pierre-the-py-pirate-solve-this-knapsack-problem-7jo) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/misc/web_scraping.py)

No, not actually dive in. Beautiful Soup is a webscraping Python library, and however difficult you thought webscraping would be, Beatiful Soup makes it so much easier. For instance, I used it on one [project](https://github.com/erik-hei/lyrical), when I had to scrape the Genius website, since their API doesn't actually provide song lyrics (I know right? You had one job, Genius). 

Let's look at a sample technical interview question:


	# Crawl a webpage and print the most common word with 
	# the count of that word.
	
	# Page to crawl:
	# https://en.wikipedia.org/wiki/Microsoft
	
	# Only words from the section “history” should be accounted for.
	
	# Example of the expected result
	#     # of occurrences
	# The 205
	
We're given the Microsoft wikipedia page, and we want to find the most common word in the "history" section. So let's get started. 

## 1. Setup and Installation

First we need to import Beautiful Soup. Install from the command line via `pip install bs4` (or however you have pip configured) Check the [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) if you're having issues with installation. 

Then, let's require our library at the top of the code. Here's everything we'll need:

	from bs4 import BeautifulSoup, Tag
	import requests
	
	from collections import defaultdict

Next, we're ready to define our function.

	def find_most_common():


## 2. Get the Page

Let's get our page and parse it with Beautiful soup. To get the page, we use the `requests` library:

	  page = requests.get("https://en.wikipedia.org/wiki/Microsoft")

Next, we parse the page text using BeautifulSoup.

	  soup = BeautifulSoup(page.text, "html.parser")
	  
How do we get just the history section? We have to take a look at the HTML of the page. There's a lot of random-looking gibberish, which I've tried to clean up:

	<h2>
		<span class="mw-headline" id="History">History</span>
	</h2>
	<div ...>...</div>
	<div ...>...</div>
	<h3>
		<span ...></span>
		<span class="mw-headline" id="1972–1985:_Founding">1972–1985: Founding</span>
	</h3>
	.
	.
	.
	<p>Childhood friends <a href="/wiki/Bill_Gates" title="Bill Gates">Bill Gates</a> and <a href="/wiki/Paul_Allen" title="Paul Allen">Paul Allen</a> sought to make a business using their skills in <a href="/wiki/Computer_programming" title="Computer programming">computer programming</a>.....

For some reason, Wikipedia seems to have all their content in one div. This means that the "history" section is not its own div, but a header and some stuff inside a parent div, which contains all the sections. To get only the history section, the best we can do for now is to just grab that header and everything after it. We grab the `<span>` tag with ID "History", and then go to its parent, the `<h2>`. To get everything after it, we can use the BeautifulSoup notation, `next_siblings`. Altogether:

	  history = soup.find(id="History").parent.next_siblings
	  
## 3. Count the Words

Let's initialize a couple variables. We'll need the most common word and the number of times it appears. We'll also use a dictionary to store the count of each word. Knowing me, we'll use a default dicitonary for this (as a review, the we can set the default type to integers, so if we access a key with no values, the defalut value is 0). 

	  max_count = 0
	  max_word = ""
	  dd = defaultdict(int)
	
Now, we're ready to crawl. Let's loop through `history` and look at each element, `elem`. However, Beautiful Soup sometimes returns something called a "Navigable String" instead of an element. We'll filter out everything that isn't an element using the `isinstance()` method from out library.

	  for elem in history:
	    if isinstance(elem, Tag):
	        
Let's think of what happens next. We need to look at the text for each element in history, and count the instance of each word. However, remember, we need to stop when we're no longer in the history section. The next section is the same div, but starts with an `<h2>` tag. Then, we can end the function by printing the most common word and its count. I'll return `max_count`.

	  for elem in history:
	    if isinstance(elem, Tag):
	      if elem.name == "h2":
	        print(max_word, "is the most common, appearing", max_count, "times.")
	        return max_count
	        
But what if it's not the end of the section? We need to get the text by calling the BeautifulSoup `get_text()` method, and then split it into words by calling `split()` on each space. 

	      words = elem.get_text().split()
	      
What's next? Loop through each word and update its count in the dictionary. Since we're using a dictionary, we don't have to check to see if the word is already in there before adding 1 to it. Also, don't forget to update the `max_word` and `max_count` if we find a word that's more common than what we had previously. 

	      for word in words:
	        dd[word] += 1
	        if dd[word] > max_count:
	          max_count = dd[word]
	          max_word = word 

And that's it! The code should work...unless Wikipedia changes the layout of their site. I'll add a final check at the end in case that happens. Altogether:
	
	from bs4 import BeautifulSoup, Tag
	import requests
	
	from collections import defaultdict
	
	def find_most_common():
	  page = requests.get("https://en.wikipedia.org/wiki/Microsoft")
	  soup = BeautifulSoup(page.text, "html.parser")
	  history = soup.find(id="History").parent.next_siblings
	  max_count = 0
	  max_word = ""
	  dd = defaultdict(int)
	
	  for elem in history:
	    if isinstance(elem, Tag):
	      if elem.name == "h2":
	        print(max_word, "is the most common, appearing", max_count, "times.")
	        return max_count
	      words = elem.get_text().split()
	      for word in words:
	        dd[word] += 1
	        if dd[word] > max_count:
	          max_count = dd[word]
	          max_word = word
	
	  return "Error"

## Try it out

This function prints the result, so we can simply run it with `find_most_common()`. Running the code gives us the result:


	the is the most common, appearing 221 times.
	  
	  
And there you have it! Granted, this function only works for this specific page, at the time of writing this--the main problem with web crawling is that it can break if the website owner alters their content in the slightest fashion. We also didn't account for casing or punctuation. Just a few things to think about. See you next time!

[< Week 17: Knapsack](https://dev.to/erikhei/help-pierre-the-py-pirate-solve-this-knapsack-problem-7jo) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/misc/web_scraping.py)



*Erik Heikkila is a Teaching Assistant at General Assembly. This blog is not associated with GA.*