# Create a clas E2dvector and use it to create another class representing a 3-d vector.

class E2dVector:
    @classmethod
    def __init__(self,i,j):
        self.i = i
        self.j = j
        
    def showVector(self):
        print(f"The vector is {self.i}i + {self.j}j")

class E3dVector(E2dVector):
    def __init__(self,i,j,k):
        print("3d Vector")
        super().__init__(i,j)
        self.k = k
        
    def show3dVector(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = E2dVector(10,12)
a.showVector()
b = E3dVector(11,21,34)
b.show3dVector()

