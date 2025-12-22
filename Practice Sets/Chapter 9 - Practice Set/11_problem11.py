with open("this.txt") as f:
    f1 = f.read()
    
with open("rename_by_python.txt", "w") as f:
    f.write(f1)