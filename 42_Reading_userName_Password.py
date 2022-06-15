f = open("userdetails.txt", "r")

# f.read() will read the entire details from the file
# f.readLine() will read a line from the file
# print(f.read())
# print(f.readline())
# print(f.readline())

print(f"Username: {f.readline()}Password: {f.readline()}")