# Function to Print Multiplication table of a given number. 

'''
5 X 1 = 5
'''

def Multi_Table(num):
    for i in range(11):
        print(f" {num} * {i} = {num * i}")

i = int(input("Enter a number : "))
Multi_Table(i)
