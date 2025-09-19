# If else Condition in python 

name = input("Enter your name: ")
age = int(input("Enter your Age: "))

if(age>= 18):
    print(f"{name}, you are allowed to vote")
    print(f"{name}, Voting is your Right & Duty.")
else:
    print(f"Sorry, {name} you can't vote now")

print("-"*5,"Have A Nice Day", "-"*5)
