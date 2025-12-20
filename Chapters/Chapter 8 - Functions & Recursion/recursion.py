# Recursion is a function which calls itself to get a value 

'''
n! = n*(n-1)!
factorial(n) =  n * factorial(n-1)
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(3) = 3 X 2 X 1
factorial(2) = 2 X 1
factorial(1) = 1
factorial(0) = 1 
Factorial of 0 is 1.
'''
def factorial(n):
        if(n==0 or n==1):
            return 1
        return n * factorial(n-1)
number = int(input("Enter a number : "))

if(number<0):
    print("Can't Find the Factorial of negative number.")
else:
    print(f" Factorial of {number} is {factorial(number)}")