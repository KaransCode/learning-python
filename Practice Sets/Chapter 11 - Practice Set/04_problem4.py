# Class complex to represent complex numbers, along with overloaded operators + and * which add and multiplies them

class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
        print(f"r = {r} , i = {i}")
    
    def __add__(self,c2):
        real_part = self.r + c2.r
        imag_part = self.i + c2.i
        return f"{real_part} + {imag_part}i"
    
    def __mul__(self,c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return f"{real} + {imag}i"
   
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = complex(4,5)
c2 = complex(6,7)
print(c1 + c2)
print(c1 * c2)