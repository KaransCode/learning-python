#  Create a class pets from class Animals and further create class Dog from Pets. Add a method bark to class Dog.

class Animals:
    def __init__(self):
        print("An Animal")
    
    def eat(self):
        print("Eating")
        
class Pets(Animals):
    def __init__(self):
        print("A Pet")
    
    def play(self):
        print("Playing")
        
class Dog(Pets):
    def __init__(self):
        print("A Dog")
    
    def bark(self):
        print("barking")

a = Animals()
a.eat()

b = Pets()
b.eat()
b.play()

d = Dog()
d.eat()
d.play()
d.bark()