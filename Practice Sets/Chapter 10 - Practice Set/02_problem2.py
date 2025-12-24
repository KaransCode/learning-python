class Calculator:
    def Square(self, n):
        sq = n * n
        print(f"Square of {n} is : {sq}")
        
    def Cube(self, n):
        cube = n * n * n
        print(f"Square of {n} is : {cube}")
        
    def Square_root(self, n):
        self.sq_root = n ** 1/2
        print(f"Square root of {n} is : {self.sq_root}")
        
simple = Calculator()
simple.Square(10)
simple.Cube(9)
simple.Square_root(64)
        
    
        