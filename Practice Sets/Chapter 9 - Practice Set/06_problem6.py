with open("log.txt") as file:
    log = file.read()

if("python" in log):
    print("Yes, python is present")
else:
    print("No, python is not present")
