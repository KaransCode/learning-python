# def generateTable(n):
#     table = f"Table of {n} \n"
#     for i in range(1,11):
#         table += f"{n} * {i} = {n*i}\n"
#     with open(f"Tables/table_ {n}", "w") as file:
#         file.write(table)


# for i in range(2, 20):
#     generateTable(i)
    

def Table(n):
    print(f"Table of {n} \n")
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}\n")
        
Table(88)