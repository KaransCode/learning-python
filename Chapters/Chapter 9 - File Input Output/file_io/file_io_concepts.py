# file_io_concepts.py

# ----------- 1. Writing to a file (Overwrites if exists) -----------
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

print("✅ File written in 'w' mode.")

# ----------- 2. Reading a file -----------
with open("example.txt", "r") as file:
    content = file.read()
    print("\n📖 Reading file content:\n", content)

# ----------- 3. Appending to a file -----------
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")

print("✅ Line appended using 'a' mode.")

# ----------- 4. Reading line by line -----------
with open("example.txt", "r") as file:
    print("\n📄 Reading line-by-line:")
    for line in file:
        print(line.strip())

# ----------- 5. Using readlines() and writelines() -----------
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("lines.txt", "w") as f:
    f.writelines(lines)

with open("lines.txt", "r") as f:
    print("\n📚 Contents using readlines():")
    for line in f.readlines():
        print(line.strip())

# ----------- 6. Using seek() and tell() -----------
with open("example.txt", "r") as f:
    print("\n📌 File pointer at:", f.tell())
    print("📜 First 10 chars:", f.read(10))
    print("📌 Pointer after reading 10 chars:", f.tell())
    f.seek(0)
    print("📌 Pointer reset using seek(0):", f.tell())

# ----------- 7. File existence check before reading -----------
import os

filename = "does_not_exist.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print(f"\n❌ File '{filename}' does not exist.")

# ----------- 8. Error handling with try-except -----------
try:
    with open("example.txt", "r") as f:
        print("\n🧪 Trying to read file...")
        print(f.read())
except FileNotFoundError:
    print("⚠️ File not found!")
except IOError:
    print("⚠️ An I/O error occurred!")

# ----------- 9. Creating a file if not exists -----------
filename = "new_file.txt"
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("This is a new file created only if it did not exist.")
    print(f"\n✅ '{filename}' created.")
else:
    print(f"\nℹ️ '{filename}' already exists.")

# ----------- 10. Deleting a file -----------
delete_file = "delete_me.txt"
with open(delete_file, "w") as f:
    f.write("This file will be deleted.")

if os.path.exists(delete_file):
    os.remove(delete_file)
    print(f"\n🗑️ File '{delete_file}' deleted successfully.")

# ----------- 11. Working with binary files -----------
with open("binary_file.bin", "wb") as f:
    f.write(b"This is binary content.\n")

with open("binary_file.bin", "rb") as f:
    binary_data = f.read()
    print("\n📦 Binary file content:", binary_data)
