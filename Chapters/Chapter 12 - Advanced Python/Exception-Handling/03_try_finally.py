#   Use of Finally Block in exception handling 

try:
    a = int(input("Enter a Number: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("Inside Finally block")


def Useoffinally():
    try:
        a = int(input("Enter a Number: "))
        print(a)
        return 

    except Exception as e:
        print(e)
        return 

    finally:
        print("Finally block running...")
        # In function, even if we use return in try or except block. The finally block will run difinitely.

Useoffinally()
    