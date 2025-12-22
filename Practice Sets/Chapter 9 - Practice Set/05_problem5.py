words = [ "Donkey" , "bad", "ganda"]

with open("censor.txt", "r") as file:
    content = file.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("censor.txt", "w") as file:
    file.write(content)