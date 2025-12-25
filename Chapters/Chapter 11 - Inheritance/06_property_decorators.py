#  Property Decorators

class Users:
    role = "user"
     
    @classmethod
    def show(cls):
        print(f"This is {cls.role}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname} "
    
    @name.setter
    def name(self, value):
        self.fname=  value.split(" ")[0]
        self.lname = value.split(" ")[1]

u = Users
u.show()
u.name = "Karan Singh"
print(u.name)
