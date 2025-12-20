# Program to print the following star pattern for n = 4

''' 
To print the following star pattern for n = 4
****
***
**
*
'''

def Star_pattern(num):
    if(num == 0):
        return
    print("*" * num)
    return Star_pattern(num-1)
    
user = int(input("Enter a number: "))
Star_pattern(user)