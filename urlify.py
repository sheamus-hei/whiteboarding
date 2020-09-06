# Write a method to replace all spaces in a string with '%20'. 
# Ignore any additional white space at the beginning or end of the string.

def urlify(our_string):
  # remove whitespace
  our_string = our_string.strip()
  str_list = [char for char in our_string]
  # make a new string to add each character onto so we don't have to traverse the list again
  new_string = ""
  for i in range(len(str_list)):
    if str_list[i] == " ":
      str_list[i] = "%20"
    new_string += str_list[i]
  return new_string

#print(urlify("Mr John Smith "))
# -> "Mr%20John%20Smith"