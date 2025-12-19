# Program to greet all the person
# whose name starts with S from a list l1
names = ["Karan","Shubham", "Surbhi", "Tinku","Saurav"]
greet = "Good Morning"

for name in names:
    if(name[0] == "S"):
        print(f"{greet}, {name}")
    else:
        continue
    
    