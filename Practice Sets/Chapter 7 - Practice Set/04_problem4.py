# Program to find out if a number is prime or not

number = int(input("Enter a number: "))
isPrime = True

if number > 1:
    for i in range(2,number):
        if(number%i == 0):
            isPrime = False
            break
else:
    isPrime = False
    
if(isPrime):
    print(f"{number} is Prime Number")
else:
    print(f"{number} is not a  Prime Number")
    