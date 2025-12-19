#  To print table of a given number using while loop

number = int(input("Enter the number you want table of :"))
# number = 18
i=0
while(i<11): 
    print(f"\t{number} * {i} = {number * i} ")
    i+=1

print(f"Table of {number} printed")