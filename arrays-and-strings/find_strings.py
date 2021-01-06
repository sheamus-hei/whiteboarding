# hackerrank challenge here: https://www.hackerrank.com/challenges/find-strings/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def find_strings(words, k):
  # find all substrings and put them in union set
  # a
  # b ab
  # c bc abc
  s = set()
  for word in words: 
    word_s = find_substrings(word)
    for substr in word_s:
      s.add(substr)  
  subsets = [word for word in s]
  subsets.sort()
  print(subsets)
  # build return array that returns string in set at each
  final = []
  for index in k:
    if index < len(subsets):
      final.append(subsets[index])
    else:
      final.append('INVALID')
  return final


def find_substrings(word):
  s = set()
  s.add('')
  for letter in word:
    new_set = s.copy()
    for substr in new_set:
      s.add(substr + letter)
  s.remove('')
  return s

w = ['abc', 'cde']
k = [1, 5, 20]

print(find_strings(w,k))