# Use of Global keyword 

age = 20  # global variable
def fun():
    age = 51 # local variable
    print(age)

print(age)
print(id(age))
fun()

a = 20  # global variable
def fun():
    global a 
    a += 10 # local variable
    print(a)

print(a)
fun()