message = "weLcome to KiT"

# Converting all the letters to upper case
print(message.upper())

# Converting all the letters to lower case
print(message.lower())

# Capitalizing the text
print(message.capitalize())

# Casefolding the text
print(message.casefold())

# Centering the string
# print(message.center(25,"."))
print(message.center(50))

# Finding the index of the searhing string
print(message.find("KiT"))

# True or False based on the existence of the searched string
print("z" in message)

# To Replace the part of text in the given string
message2 = message.replace("KiT", "KIT")
print(message)
print(message2)