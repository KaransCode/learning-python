# 

class Programmer:
    company = "Microsoft"
    
    def __init__(self):
        self.name = input("Enter Your Name: ")
        self.emp_id = int(input("Enter Your Employee ID: "))
        self.emp_salary = int(input("Enter Your Salary: "))
        self.emp_exp = int(input("Enter Your Work Experience : "))
        
        
        print(f"{self.name} is working at {self.company} whose Employee ID is {self.emp_id} and has {self.emp_exp} years of Experience with Salary of {self.emp_salary} Lakh rupees.")
        
    def work(self):
        print("Employee is working...")
            
    def sleep(self):
        print("Employee is sleeping...")
            
Karan = Programmer()
Karan.work()

Rohan = Programmer()
Rohan.sleep()
        