with open("poems.txt") as file:
    content = file.read()
    if("twinkle" in content):
        print("Yes, it contains the word twinkle")
    else:
        print("No, it does not contains the word twinkle")