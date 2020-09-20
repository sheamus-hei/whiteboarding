class AnimalShelter:
  def __init__(self):
    self.dogs = []
    self.cats = []
    self.order = 0
  
  def add_animal(self, name, kind):
    kind = kind.lower()
    self.order += 1;
    animal = {
      "name": name,
      "type": kind,
      "order": self.order
    }
    if kind == "cat":
      self.cats.append(animal)
    elif kind == "dog":
      self.dogs.append(animal)
    else:
      print("Invalid animal type entered. Animals must be cat or dog.")

  def __adopt_animal(self, animal_list):
    if len(animal_list) == 0:
      return None
    else:
      return animal_list.pop(0)

  def adopt_dog(self):
    return self.__adopt_animal(self.dogs)

  def adopt_cat(self):
    return self.__adopt_animal(self.cats)

  def adopt_any(self):
    if len(self.cats) == 0:
      return self.adopt_dog()
    elif len(self.dogs) > 0 and self.cats[0]["order"] > self.dogs[0]["order"]:
      return self.adopt_dog()
    else:
      return self.adopt_cat()
  
a = AnimalShelter()
a.add_animal("Kai", "cat")
a.add_animal("JJ", "Dog")
a.add_animal("Sushi", "Cat")
a.add_animal("Pickles", "Dog")
print(a.cats, a.dogs)
a.adopt_cat()
a.adopt_dog()
a.adopt_any()
print(a.cats, a.dogs)