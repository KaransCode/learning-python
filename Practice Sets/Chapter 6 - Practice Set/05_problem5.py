#  Program to find out whether a given name is 
#  already present in a list 

name_list = ["Ankit", "Bhuvan", "Karan", "Rohan", "Sumit"]

user_name = input("Enter your name: ")

if(user_name in name_list):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")
