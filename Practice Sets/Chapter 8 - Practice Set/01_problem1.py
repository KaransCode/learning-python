# Program to find the greatest of three numbers. 

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if(c>b and a<c):
        return c
x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2nd number: "))
z = int(input("Enter the 3rd number: "))
great = greatest(x,y,z)
print(f"Greatest number is {great}")
    