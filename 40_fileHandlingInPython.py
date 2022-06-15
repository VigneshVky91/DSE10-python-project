def createMyFile():
    myFile = open("testfile.txt", "a")
    print(myFile)

    myFile.write("\nThis is new statement")

createMyFile()