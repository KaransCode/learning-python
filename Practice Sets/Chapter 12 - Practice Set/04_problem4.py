try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = a/b
    print(c)

except ZeroDivisionError as z:
    print("Infinite", z)

else:
    print("Program ran successfully") 