message = ""

while True:
    msg = input("Input any text to write to the file\nand q to stop inputting")
    if msg == 'q' or msg =='Q':
        break
    else:
        message = message+'\n'+msg

f = open("multiline_file.txt", "w")
f.write(message)