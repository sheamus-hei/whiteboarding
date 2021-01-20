# The goal of this challenge is to implement a console application that displays the most common words used in a portion of a webpage.
# Requirements
# The code should be written in Python.
# The code should return the most common words used and the number of times they are used. The following should be configurable:
# -   The number of words to return (default: 10)
# -   Words to exclude from the search
# Your code (only the source code, no binaries) should be returned as a zip.  The code should build into an executable console application. 
# Page to crawl
# https://en.wikipedia.org/wiki/Microsoft
# Only words from the section “history” should be accounted for.
# Example of the expected result
#     # of occurrences
# The 205
# Microsoft   113
# in  110
# of  88
# and 88
# a   81
# to  79
# on  59
# Windows 55
# for 50
from collections import defaultdict

from bs4 import BeautifulSoup, Tag
import requests

def find_most_common():
  page = requests.get("https://en.wikipedia.org/wiki/Microsoft")
  soup = BeautifulSoup(page.text, "html.parser")
  #soup = [s.extract() for s in soup('script')]
  history = soup.find(id="History").parent.next_siblings
  max_count = 0
  max_word = ""
  dd = defaultdict(int)

  for elem in history:
    if isinstance(elem, Tag):
      if elem.name == "h2":
        print(max_word, "is the most common")
        return max_count
      words = elem.get_text().split()
      for word in words:
        dd[word] += 1
        if dd[word] > max_count:
          max_count = dd[word]
          max_word = word

  return "Error"
    

print(find_most_common())