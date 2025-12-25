#  Operator Overloading in Python
'''
1. Operators in Python can be overloaded using dunder Methods
2. These Methods are called when a given operator is used on the objects
3. Operators in Python can be overloaded using the following Methods:

p1 + p2 -> p1.__add__(p2) 
p1 - p2 -> p1.__sub__(p2) 
p1 * p2 -> p1.__mul__(p2) 
p1 / p2 -> p1.__truediv__(p2) 
p1 // p2 -> p1.__floordiv__(p2) 

Other dunder/ magic methods in Python:
__str__() 
__len__() 
'''

class Number:
    def __init__(self, n):
        self.n = n
        print(f"Number =  {self.n}")
        
    def show(self, n):
        self.n = n
        print(f"Number =  {self.n}")
    
    def __add__(self,num):
        return self.n + num.n

m = Number(3)
n = Number(12)

print(m.__add__(n))