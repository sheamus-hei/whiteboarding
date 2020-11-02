class Node:
  def __init__(self, data):
    self.next = None
    self.data = data

  def append(self, val):
    end = Node(val)
    n = self
    while (n.next):
      n = n.next
    n.next = end

# Node class with more obfuscation
# class Node:
#   def __init__(self, data):
#     self.next = None
#     self.__data = data

#   def set_data(self, val):
#     self.__data = val

#   def get_data(self):
#     return self.__data

#   def append(self, val):
#     end = Node(val)
#     n = self
#     while (n.next):
#       n = n.next
#     n.next = end


# Remove Dups: Write code to remove duplicates from an unsorted linked list
from collections import defaultdict
def remove_dups(front):
  counted = defaultdict(bool)
  temp = front
  counted[temp.data] = True
  while (temp.next):
    # check the value of next Node
    # print("CHECKING", temp.data)
    if (counted[temp.next.data]):
      #if found in dictionary, remove it
      temp.next = temp.next.next
    else:
      counted[temp.next.data] = True
      temp = temp.next
  # print(dd)

ll = Node(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(1)
ll.append(4)

remove_dups(ll)

node = ll
print(node.data)
while node.next:
    node = node.next
    print(node.data)