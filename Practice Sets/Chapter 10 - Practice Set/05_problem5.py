from random  import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        print("Welcome to Indian Railways.")
    
    def book(self,tfrom, to):
        print(f"Train is booked in Train No. {self.trainNo} From {tfrom} to {to}.")
        
    def getStatus(self):
        print(f"Train No. {self.trainNo} is running on time.")
        
    def getFare(self):
        print(f"Train Fare for Train No. {self.trainNo} is {randint(500,2000)} ")

t1 = Train(121221)
t1.book("Delhi", "Mumbai")
t1.getStatus()
t1.getFare()