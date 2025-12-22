with open("this.txt") as f:
    content = f.read()

with open("that.txt", "w") as f:
    f.write(content)   
