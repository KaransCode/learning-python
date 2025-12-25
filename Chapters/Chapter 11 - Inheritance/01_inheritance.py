# Inheritance is the process to create a new class from existing class or base class.

class Employee:  # Base or Parent Class
    company = "Google"
    def show(self, name, salary):
        self.name = name 
        self.salary = salary
        print(f"The name of the employee is {self.name} and the salary of the employee is {self.salary}")


class Programmer(Employee):   # Derived or Child Class
    company = "Microsoft"
    def showLanguage(self, name, language):
        self.name = name
        self.language = language
        print(f"{self.name} is good at {self.language} Language.")
        
a = Employee()
print(a.company)
a.show("Karan",1200000)

b = Programmer()
print(b.company)
b.showLanguage("Narak", "Python")

#  Types of Inheritance 
# 1. Single       A -> B
# 2. Multiple     A & B -> C
# 3. Multi-Level  A -> B -> C