name = input("Input your name: ")
print(name)

# Extracting the first character of the string
print(f"The first character of the string entered: {name[0]}")

# Extracting the last character of a string
print(f"The last character of the string entered: {name[len(name)-1]}")

# Extracting the first character of the string using negative indexing
print(f"The first character of the string entered: {name[-(len(name))]}")

# Extracting the last character of a string using negative indexing
print(f"The last character of the string entered: {name[-1]}")
