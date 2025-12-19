# To print star pattern using loop 
'''
*
**
***
'''

n=int(input("Enter a number: "))

# for i in range(0,n+1):
#     print("*"*i, end="")
#     print(" ")
    
for i in range(n,0,-1):
    print("*"*i, end="")
    print(" ")