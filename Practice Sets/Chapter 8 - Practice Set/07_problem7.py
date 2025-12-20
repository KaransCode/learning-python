# Function to remove a given word from a list 
# and strip it at the same time. 

'''
list = ["Apple", "Nimbu", "Banana", "Mango"]
word = "Nimbu"
list = ["Apple", "Banana", "Mango"]

'''
lt = ["Apple", "Nimbu", "Banana", "Mango", "ana"      ]

def List_Strip(word):
    word = word.strip()  # Strip any leading/trailing spaces
    if word in lt:
        lt.remove(word)
        print(f"'{word}' removed from the list.")
    else:
        print(f"'{word}' not found in the list.")

print("Original list:", lt)

word = input("Enter a word to remove from the list: ")
List_Strip(word)

print("Updated list:", lt)

l = ["Seb", "Pineapple", "Banana", "Aam", "ana"      ]
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
        return n

print(rem(l, "ana"))
