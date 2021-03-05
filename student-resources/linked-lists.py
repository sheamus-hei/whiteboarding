# just the node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def append(self, val):
    end = Node(val)
    n = self
    while (n.next):
      n = n.next
    n.next = end

# list wrapper class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # returns length of the list
    def __len__(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return '[]'

        current = self.head
        result = str(current) # what we return once we've concantenated all the nodes to it
        while current.next:
            result += f' -> {str(current.next)}'
            current = current.next
        return f'[{result}]'


# Traversal
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print(head.data)
node = head
while node.next:
    node = node.next
    print(node.data)

# using recursion
def traversal(node):
  if node:
    print(node.data)
    traversal(node.next)

traversal(head)

from collections import defaultdict
def remove_dups(front):
  counted = defaultdict(bool)
  temp = front
  counted[temp.data] = True
  while (temp.next):
    # check the value of next Node
    if (counted[temp.next.data]):
      #if found in dictionary, remove it
      temp.next = temp.next.next
    else:
      counted[temp.next.data] = True
      temp = temp.next

head.append(3)
head.append(4)
remove_dups(head)
traversal(head)
