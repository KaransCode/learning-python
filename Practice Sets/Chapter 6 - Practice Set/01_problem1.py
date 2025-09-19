# Program to find the greatest of 4 numbers entered by user 

num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))
num3 = int(input("Enter your 3rd number: "))
num4 = int(input("Enter your 4th number: "))

print(f"number1 = {num1}")
print(f"number2 = {num2}")
print(f"number3 = {num3}")
print(f"number4 = {num4}")

if(num1 > num2 and num1 > num3 and num1 > num4):
    print(f"{num1} is the greatest from all.")
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print(f"{num2} is the greatest from all.")
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print(f"{num3} is the greatest from all.")
else:
    print(f"{num4} is the greatest from all.")

print("--Program Ends Here--")

