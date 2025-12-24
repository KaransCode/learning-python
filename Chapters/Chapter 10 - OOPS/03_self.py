class Employee:
    Emp_name = ""
    Emp_code = ""
    Emp_language = ""
    salary = ""
    
    def Emp_salary(self):
        print(f"Employee's Salary is {self.salary}")

karan = Employee()
karan.Emp_name = "Narak"
karan.salary = 19010120

print(karan.Emp_name, karan.salary)
karan.Emp_salary()