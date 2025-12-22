# using readline() function 
with open("test.txt") as file:
    for line in file:
        print(line.strip())
      
      
# using readlines() function   
with open("test.txt") as file:
    print(file.readlines())
    