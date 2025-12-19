#  Program to print multiplication table of a given number

# number = 18
number = int(input("Enter the number you want table of :"))

for i in range(11):
    result = number * i
    print(f"\t{number} * {i} = {result} ")

print(f"Table of {number} printed")