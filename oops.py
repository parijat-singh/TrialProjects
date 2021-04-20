'''
Created on Feb 13, 2021

@author: parij
'''
class Animal:
    eyes = 2
    
    def talk(self):
        return "Animal talk"
    
dog = Animal()
print("dog has " + str(dog.eyes) + " eyes")

class Dog(Animal):
    legs = 4
    
    def talk(self):
        return "Woof"

bingo = Dog()
print("Bingo has " + str(bingo.eyes) + " eyes")
print("Bingo has " + str(bingo.legs) + " legs")
print("Bingo says " + bingo.talk())

class Shape:
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth

l = int(input("Enter Length: "))
b = int(input("Enter breadth: "))
rectangle = Shape(l,b)
print(rectangle.area())