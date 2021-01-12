# find the best prefix match for each phone number given as an input. 
# If there is no prefix match for a given phone number, return an empty string.    

# Inputs:     
# prefixes: an array of strings    
# numbers: an array of strings    
# general case with len > 1 for prefixes and numbers


# Iterative solution by Karly
def match2(prefixes, numbers):
        
        #make a new list to save the matching prefixes
	    matching = [] 
	    
	    # iterate through numbers to find a match for each
	    for i, num in enumerate(numbers): 
              while len(num) > 1: 
                if num in prefixes: 
                      # take the first prefix value that matches
                    matching.append(num)
                    break
                num = num[:-1] 

              if len(matching) < i + 1: 
                  # add an empty string if no match is found
                matching.append("")
        
	    return matching

# my brute force solution using startswith()
def match3(prefixes, nums):
  matching = []
  for num in nums:
    appended = False
    for prefix in prefixes:
      if num.startswith(prefix):
        if appended == False:
          appended = True
          matching.append(prefix)
        elif len(matching[-1]) < len(prefix):
          matching[-1] = prefix
    if appended == False:
      matching.append("")
  return matching

# I altered Karly's solution to use a recursive helper method
def helper(prefixes, num):
  if len(num) == 0:
    return ""
  elif num in prefixes: 
    return num
  else:
    return(helper(prefixes, num[:-1]))

def matchRecursive(prefixes, numbers):
  matching = [] 
  for num in numbers: 
    matching.append(helper(prefixes, num))
  return matching  


prefixes1 = ['+1415123', '+1415000', '+1412', '+1510', '+1', '+44']        
numbers1 = ['+14151234567', '+99999999999', '+14121234567', '+19999999999']        
print(matchRecursive(prefixes1, numbers1))

# -> ['+1415123', "", '+1412', '+1']
