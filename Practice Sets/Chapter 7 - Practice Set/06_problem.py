#  To find the factorial of a given number using for loop

n = int(input("Enter a number: "))
fact = 1

if(n==0):
    fact = 1
elif(n<0):
    print("You can't calculate factorial for a negative number")
else:
    for i in range(n,0,-1):
        fact *= i


print(f"Factorial of {n} is {fact}")