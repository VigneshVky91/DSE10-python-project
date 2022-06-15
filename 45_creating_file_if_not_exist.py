import os

f = open("newfile.txt", "x")

if os.path.exists():
    f = open("newfile.txt", 'r')
    print(f.read())
else:
    f = open("newfile.txt", "x")
    print("File created successfully...")
