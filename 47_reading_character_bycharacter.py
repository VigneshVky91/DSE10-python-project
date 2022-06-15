source = open("source.txt", "r")
destination = open("destination.txt", "w")
while True:
    myChar = source.read(1)
    if not myChar:
        break
    else:
        destination.write(myChar+"\n")