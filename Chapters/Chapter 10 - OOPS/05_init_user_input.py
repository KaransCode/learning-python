class Student:
    
    def __init__(self):
        self.name = input("Enter your name: ")
        self.id =  int(input("Enter your ID: "))
        self.age =  int(input("Enter your Age: "))
        self.sclass = input("Enter your Class name: ")
        print(f"\n Student Name is : {self.name} \n Student id is {self.id} \n Student Age is {self.age}. \n Student's Class is {self.sclass}")
        
    def study(self):
        print(f"\n Student is Studying....")

print("----"*10)
print("Student's Details Loading... \n ")
karan = Student()
karan.study()
print("----"*10)

