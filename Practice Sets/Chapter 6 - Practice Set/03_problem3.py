# Program to check spam comments 
# having given keywords

key1 = "buy now"
key2 = "click this"
key3 = "subscribe now"
key4 = "get money"
key5 = "click this link"

comment = input("Enter a comment: ")

if(key1 in comment or key2 in comment or key3 in comment or key4 in comment or key5 in comment):
    print("This comment is spam!!!")
else:
    print("This comment is okay.")

