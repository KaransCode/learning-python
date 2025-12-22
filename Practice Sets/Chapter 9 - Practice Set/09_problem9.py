with open("this.txt") as f:
    f1 = f.read()
    
with open("poem.txt") as f:
    f2 = f.read()
    
if(f1 == f2):
    print("Yes, these file are identical")
else:
    print("No, these file are not identical")
    
