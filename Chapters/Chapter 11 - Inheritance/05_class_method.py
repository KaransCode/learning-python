#  class method is a method which is bound to use class attribute and not the object of the class.

class Person:
    species = "Homo Sapiens"
    @classmethod
    def show(cls):
        print(f"It has speci of {cls.species}")
        
class Student(Person):
    def desc(self):
        print(f"I am a Student.")

p = Person()
p.show()
p.species = "Mammals"
p.show()

s = Student()
s.desc()
s.species = "Reptile" # The Change will not be affected because of @classmethod attribute
s.show()
