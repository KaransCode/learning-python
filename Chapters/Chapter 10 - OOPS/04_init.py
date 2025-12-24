class Student:
    
    def __init__(self, name, id, age, sclass ):
        self.name = name
        self.id =  id
        self.age =  age
        self.sclass = sclass
        print(f"Student Name is : {name} \n Student id is {id} \n Student Age is {age}. \n Student's Class is {sclass}")
        
    def study(self):
        print(f"\n Student is Studying....")


print("Before Creating object.\n ")
print("Student's Details Loading...\n ")
karan = Student("Karan Singh", 1020, 21, "MCA-DS")
karan.study()

