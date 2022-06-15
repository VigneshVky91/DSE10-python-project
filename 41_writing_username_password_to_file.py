def writeUserDetails(userName, password):
    f = open("userdetails.txt", "w")
    f.write(userName)
    f.write('\n'+password)

writeUserDetails("Daravuth", "Dara@123")