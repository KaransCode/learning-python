try:
    with open("1.txt") as file:
        print(file.read())
except Exception as e:
    print(e)
    
try:
    with open("2.txt") as file:
        print(file.read())
except Exception as e:
    print(e)
    
try:
    with open("3.txt") as file:
        print(file.read())
except Exception as e:
    print(e)

else:
    print("File Accessing is Done.")
