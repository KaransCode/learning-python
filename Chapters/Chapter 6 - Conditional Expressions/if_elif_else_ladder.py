# If elif else ladder in python 

name = input("Enter your name: ")
age = int(input("Enter your Age: "))

if(age>= 18):
    print(f"{name}, you are allowed to vote")
    print(f"{name}, Voting is your Right & Duty.")
elif(age<0):
    print(f"Sorry,{name} Age can't be less than 0 or -ve")
elif(age==0):
    print(f"Listen,{name} Are you 0 years old or is this you IQ :)")
else:
    print(f"Sorry, {name} you can't vote now")

print("-"*5,"Have A Nice Day", "-"*5)
