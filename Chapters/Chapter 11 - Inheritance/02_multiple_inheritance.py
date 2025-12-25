# In Mulitple Inheritance, base class can take methods of two parent class.

class Employee:  # Base or Parent Class
    company = "Google"
    def __init__(self):
        print("\n I am an Employee. I have a Job to do.")
    def show(self, name, salary):
        self.name = name 
        self.salary = salary
        print(f"The name of the employee is {self.name} and the salary of the employee is {self.salary}")
        
        
class Coder:  # Base or Parent Class
    exp = "3 Years"
    def __init__(self):
        print("\n I am Coder. I love Coding at free time.")
        
    def printLanguage(self, language):
        self.language = language
        print(f"My Favorite Langauge is {language}")


class Programmer(Employee, Coder):   # Derived or Child Class
    company = "Microsoft"
    def __init__(self):
        print("\n I am Programmer. I love Programming.")
        
    def showLanguage(self, name, language):
        self.name = name
        self.language = language
        print(f"{self.name} is good at {self.language} Language.")
        
a = Employee()
print(a.company)
a.show("Karan",1200000)

c = Coder()
print(c.exp)
c.printLanguage("C")

b = Programmer()
print(b.company)
b.showLanguage("Narak", "Python")
b.exp = "5 years"
print(b.exp)
b.language
b.printLanguage("C++")