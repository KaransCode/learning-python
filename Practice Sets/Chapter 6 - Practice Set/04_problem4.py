# Check whether a username contains 10 characters

user_name = input("Enter your username: ")

if(len(user_name) < 10 ):
    print("Your user name contains less than 10 characters")
else:
    print("Everything is fine")