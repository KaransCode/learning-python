# Program to find sum of first n natural number using recursion 

'''
Sum(n) = n + (n-1) + (n-2) + (n-3) .... 3 + 2 + 1.
Sum(5) = 5 + 4 + 3 + 2 + 1 = 15
Sum(4) = 4 + 3 + 2 + 1 = 10
Sum(3) = 3 + 2 + 1 = 6
Sum(2) = 2 + 1 = 3

'''

def Sum_of_natural_num(num):
    if(num==1):
        return 1
    return num + Sum_of_natural_num(num-1)

user = int(input("Enter a Natural number: "))
print(f"Sum of first {user} Number is {Sum_of_natural_num(user)}.")