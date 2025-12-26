n = int(input("Enter a number: "))

with open("Table.txt" , "a") as file:
    table = [n*i for i in range(1,11)]
    print(table)
    file.write(f"Table of {n} is : {str(table)} \n")
    file.close()