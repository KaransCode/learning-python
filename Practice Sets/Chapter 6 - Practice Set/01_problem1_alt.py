# Program to find the greatest of 4 numbers entered by user 

num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))
num3 = int(input("Enter your 3rd number: "))
num4 = int(input("Enter your 4th number: "))

print(f"number1 = {num1}")
print(f"number2 = {num2}")
print(f"number3 = {num3}")
print(f"number4 = {num4}")

greatest = num1
if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
    greatest = num1
elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
    greatest = num2
elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
    greatest = num3
else:
    greatest = num4

print(f"{greatest} is the greatest number of all")
print("--Program Ends Here--")

