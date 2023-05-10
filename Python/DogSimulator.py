class Dog:
  def __init__(self, name, age, gender, temperment, food, medications):
    self.name = name
    self.age = age
    self.gender = gender
    self.temperment = temperment
    self.food = food
    self.medications = medications
  
  def bark(self):
    print("Woof!")
