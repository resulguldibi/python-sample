
from lib import animal

class Dog(animal.Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("howw !! my name is  " + self.name + " and I am "+ str(self.age) + " years old.")