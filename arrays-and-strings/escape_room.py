# 1. Escape Room Keypads Problem Statement You're attempting to solve a puzzle in an Escape Room with your team where you need to open a door to get to the next stage. There are several doors, each with a different keypad on it. The keypads each have 7 keys, containing 7 distinct letters. Each keypad looks like this: Enter a word AELPSXY Enter The instructions state that one of the keypads will open the correct door leading to the next stage of the game. 
# Your job is to find a word that unlocks the correct keypad. After struggling for some time, the Escape Room leader gave you a clue, that the first letter of the keypad is guaranteed to be in the word that opens Type here to search |A|EL|P|SX|Y Enter The instructions state that one of the keypads will open the correct door leading to the next stage of the game. Your job is to find a word that unlocks the correct keypad. After struggling for some time, the Escape Room leader gave you a clue, that the first letter of the keypad is guaranteed to be in the word that opens the door. We will call this letter the "key" letter. The goal of this exercise is to come up with as many words as possible that your team can test out on the keypads and find the correct combination to go the next stage of the game. What you know: • The correct combination will be a valid English word. • The words are at least 5 letters long, with no maximum length. • The "key" letter will be in the correct answer. • The words do not contain any letters outside the seven letters on the keypad. • Letters may be reused, including the "key" letter. For our purposes, we'll express each set of keypad letters as a string of length 7, where the first letter Type here to search number of valid words in the corresponding lock. 

#Constraints: 
#• Both the wordlist and the keypad letters will be supplied in all capital letters. 
#• All words in the wordlist will be of length 5 or greater. 
#• Every sequence of keypad letters will be of exactly length 7. #Every sequence of keypad letters will consist of 7 distinct letters. 
#• The "key" letter will be in the correct answer. 
#• The words do not contain any letters outside the seven letters on the keypad. 
#• Letters may be reused, including the "key" letter. 
#Performance of your solution is important! A naive solution will not get you full points - to score 100/100, you'll need something significantly faster. 

# Example Input: 
  # wordlist: ['APPLE', PLEAS', 'PLEASE'] 
  # keypads: ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY'] 
# Expected output: [0, 1, 3, 2, 0] 

from collections import defaultdict

def word_helper(word, keypad_letters):
  for letter in word:
    letter = letter.lower()
    if keypad_letters[letter] == 0:
      return 0
  print(word, "is ok")
  return 1

def word_finder(wordlist, keypads):
  outputs = []
  for keypad in keypads:
    print("Checking words for", keypad)
    keypad_letters = defaultdict(int)
    key = keypad[0].lower()
    words_contained = 0
    for letter in keypad:
      letter = letter.lower()
      # if letter in keypad_letters:
      #   letter += 1
      # else:
      #   keypad_letters[letter] = 1
      keypad_letters[letter] += 1
    for word in wordlist:
      if key in word or key.upper() in word:
        words_contained += word_helper(word, keypad_letters)
    outputs.append(words_contained)
  return outputs

words = open('dictionary.txt', 'r').read().split('\n')
# print(words)
wordlist = ['APPLE', 'PLEAS', 'PLEASE'] 
keypads = ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY']
print(word_finder(wordlist, keypads))