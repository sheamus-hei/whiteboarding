# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Trisha's solution
def isValidSudoku(board):
  numbers = {} # Counting the number of times I see a number.
  # Check if any rows have any duplicates.
  for row in board:
    for i, number in enumerate(row): 
      if number == ".": 
        continue
      elif number in numbers.keys(): # If we've already seen this number.
        return False
      elif number not in numbers.keys(): # If we're seeing a number for the first time, add it.
        numbers[number] = 1
    numbers = {}
  # Check if any columns have any duplicates.
  for col in range(len(board)): # Col = column index. 
    for row in board: 
      number = row[col]
      if number == ".": 
        continue
      elif number in numbers.keys(): # If we've already seen this number.
        return False
      elif number not in numbers: # If we're seeing a number for the first time, add it.
        numbers[number] = 1
    numbers = {}
  # Check within each demarcated 3x3 box. 
  boxes = {}
  for i, row in enumerate(board):
    for y, number in enumerate(row):
      if number != ".":
        box = str( i//3 ) + str( y//3 )
        if box in boxes.keys():
          if number in boxes[box]: # Checking if number exists in set
            return False
          else: 
            boxes[box].add(number) # Add number to set
        else:
          boxes[box] = set(number) # Create a new set
  return True

  # Erik Solution
def isValidSudoku2(board):
  numbers = set()

  # check rows
  for row in board:
    for number in row:
      if number != "." and number not in numbers:
        numbers.add(number)
      elif number != ".": # number in numbers
        return False
      numbers = set()
  
  # check columns
  for col in range(len(board)):
    for row in board:
      number = row[col]
      if number != "." and number not in numbers:
          numbers.add(number)
      elif number != ".": # number in numbers
          return False
    numbers = set()
  
  #check 3x3 square
  from collections import defaultdict
  boxes = defaultdict(set)
  for i, row in enumerate(board):
    for j, number in enumerate(row):
      if number != ".":
        box_code = str(i//3) + str(j//3)
        if number in boxes[box_code]:
          return False
        else:
          boxes[box_code].add(number)
  return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku2(board))
# -> True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku2(board))
# -> False