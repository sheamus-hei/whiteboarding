# This problem was asked by Amazon.
# Implement a stack that has the following methods:
# 1. push(val), which pushes an element onto the stack
# 2. pop(), which pops off and returns the topmost element of the stack. 
#   If there are no elements in the stack, then it should throw an error or return null.
# 3. max(), which returns the maximum value in the stack currently. 
#   If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.

class Stack:
  def __init__(self):
    self.stack = []
    self.max = None

  def pop(self):
    if len(self.stack) == 0:
      return None
    removed = self.stack.pop()
    if len(self.stack) == 0:
      self.max = None
    elif removed == self.max:
      self.max = self.stack[0]
      # *** this solution is not constant time!
      for item in self.stack:
        if item > self.max:
          self.max = item
    return removed

  def push(self, item):
    self.stack.append(item)
    if len(self.stack) == 1 or item > self.max:
      self.max = item

  def print_max(self):
    # I changed the name to print_max so Pyflakes wouldn't get angry about renaming things
    return self.max

# >>> s = Stack()
# >>> s.push(1)
# >>> s.push(2)
# >>> s.push(3)
# >>> s.max
# 3
# >>> s.pop()
# 3
# >>> s.max
# 2
# >>> s.pop()
# 2
# >>> s.max
# 1
# >>> s.pop()
# 1
# >>> s.max
# >>> print(str(s.max))
# None
# >>> 