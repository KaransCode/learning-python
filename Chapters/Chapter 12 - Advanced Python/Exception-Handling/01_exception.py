# Error Handling in Python can be addressed using try except block 

try:
    n = int(input("Enter your Age: "))
    print(n)
except Exception as e:
    print("Please enter a valid age !!", e )

print("Have A Nice day :) ")

# Types of Errors that can be handled 
# ZeroDivisionError , TypeError , ValueError , Other Type of Error

try: 
    a = 100
    b = 0
    print(a/b)
    
except ZeroDivisionError as z:
    print(z)
    