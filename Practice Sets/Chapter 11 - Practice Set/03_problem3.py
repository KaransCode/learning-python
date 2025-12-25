# Create a class employee and add Salary and increment properties to it.
#  Write a method salaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on salary

class Employee:
    salary = 150000
    increment = 20
    def __init__(self):
        print("Employee")
    
    @property
    def SalaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
        
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,salary):
        self.increment = ((salary / self.salary - 1) * 100)

e = Employee()
e.SalaryAfterIncrement = 200000
print(e.increment)
print(e.salary)
print(e.SalaryAfterIncrement)
# e.SalaryAfterIncrement = 20000