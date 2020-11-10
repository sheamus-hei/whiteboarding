import datetime
import math
import pprint
pp = pprint.PrettyPrinter(indent=4)

def make_hash(prev_hash, transactor, amount):
  return prev_hash + int(int(amount)**1.5) + ord(transactor[-1])

class Block:
  def __init__(self, prev_hash, transactor, amount):
    self.next = None
    self.__data = {
      "prev_hash": prev_hash,
      "time": datetime.datetime.now().time(),
      "transactor": transactor,
      "amount": amount,
      "hash": make_hash(prev_hash, transactor, amount)
    }
    self.__prev_hash = prev_hash

  def append(self, transactor, amount):
    n = self
    while (n.next):
      n = n.next
    prev_hash = n.get_data()["hash"]
    end = Block(prev_hash, transactor, amount)
    n.next = end

  def get_data(self):
    return self.__data

  def __update_hashes(self, new_prev):
    self.__data["prev_hash"] = new_prev
    self.__data["hash"] = make_hash(new_prev, self.__data["transactor"], self.__data["amount"])

  def set_amount(self, amount):
    self.__data["amount"] = amount
    self.__data["hash"] = make_hash(self.__data["prev_hash"], self.__data["transactor"], amount)
    temp = self
    while(temp.next):
      prev_hash = temp.__data["hash"]
      temp = temp.next
      temp.__update_hashes(prev_hash)

def print_chain(chain):
  node = chain
  pp.pprint(node.get_data())
  while node.next:
      node = node.next
      pp.pprint(node.get_data())

chain = Block(0, 'Tim', 120.00)
chain.append('Jamil', 200.00)
chain.append('Carla', 123.45)
chain.append('Sarah', 450.00)

print_chain(chain)

chain.next.set_amount(700)

print("UPDATE:")
print_chain(chain)
