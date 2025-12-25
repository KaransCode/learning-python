# Super keyword - calls the constructor of parent class
#   use to access the methods of parent class in child class

class Employee:  # Base or Parent Class
    company = "Google"
    def __init__(self):
        print("\n I am an Employee. I have a Job to do.")
        
    def show(self, name, salary):
        self.name = name 
        self.salary = salary
        print(f"The name of the employee is {self.name} and the salary of the employee is {self.salary}")
        
class Programmer(Employee):   # Parent for Manager & Child Class for Employee
    company = "Microsoft"
    def __init__(self):
        super().__init__()
        print("\n I am Programmer. I love Programming.")
        
    def showLanguage(self, name, language):
        self.name = name
        self.language = language
        print(f"{self.name} is good at {self.language} Language.")
        
class Manager(Programmer):   # Derived or Child Class
    role = "Manager"
    def __init__(self):
        super().__init__()
        print("\n I am Program Manager.")
        
    def showExp(self, name, exp):
        self.name = name
        self.exp = exp
        print(f"{self.name} has {self.exp} years of experience.")

m = Manager()


# a = Employee()
# print(a.company)
# a.show("Karan",1200000)

# b = Programmer()
# print(b.company)
# b.show("Rohan",1500000)
# b.showLanguage("Mohan", "Python")

# c = Manager()
# c.company = "Flipkart"
# print(c.company)
# c.show("Vishal",4500000)
# c.showLanguage("Vikas", "Python")
# print(c.role)
# c.showExp("Manager", "5 years")



