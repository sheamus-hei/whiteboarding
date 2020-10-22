class Stack:
  def __init__(self):
    self.top = None
  class __StackNode:
    def __init__(self, data):
      self.data = data
      self.next = None
  def pop(self):
    if (self.top == None):
      raise Exception('Cannot pop from an empty stack.')
    item = self.top.data
    self.top = self.top.next
    return item
  def push(self, new_item):
    new_node = self.__StackNode(new_item)
    new_node.next = self.top
    self.top = new_node
  def peek(self):
    if (self.top == None):
      raise Exception('Stack is empty!')
    return self.top.data
  def is_empty(self):
    return self.top == None

class Node:
  def __init__(self, data):
    self.next = None
    self.data = data
  def set_data(self, val):
    self.data = val
  def get_data(self):
    return self.data
  def append(self, val):
    end = Node(val)
    n = self
    while (n.next):
      n = n.next
    n.next = end
def is_palindrome(node):
  new_stack = Stack()
  temp = node
  while (temp):
    new_stack.push(temp.data)
    temp = temp.next
  temp = node
  while not new_stack.is_empty():
    pop_val = new_stack.pop()
    if (temp.data != pop_val):
      return False
    else:
      temp = temp.next
  return True
  
linked_list = Node('T')
linked_list.append('A')
linked_list.append('C')
linked_list.append('O')
linked_list.append('C')
linked_list.append('A')
linked_list.append('T')
print(is_palindrome(linked_list))