class Calculator:
    def __init__(self, n):
        self.n = n
        
    def Square(self):
        sq = self.n * self.n
        print(f"Square of {self.n} is : {sq}")
        
    def Cube(self):
        cube = self.n * self.n * self.n
        print(f"Square of {self.n} is : {cube}")
        
    def Square_root(self):
        sq_root = self.n ** 1/2
        print(f"Square root of {self.n} is : {sq_root}")
        
    @staticmethod
    def greet():
        print("Good Morning, How are you?")
   
    
check = Calculator(20)
check.greet()
check.Square()
check.Cube()
check.Square_root()

        
    
        