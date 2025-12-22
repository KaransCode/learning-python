word = "Donkey"

with open("donkey.txt", "r") as file:
    content = file.read()

contentNew = content.replace("####", word )

with open("donkey.txt", "w") as file:
    file.write(contentNew)