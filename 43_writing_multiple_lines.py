msg1 = "Line 1\n"
msg2 = "Line 2\n"
msg3 = "Line 3\n"

f = open("multilines.txt", "w")
f.writelines([msg1, msg2, msg3])
# f.write(" %s \n %s \n %s \n" % (msg1, msg2, msg3))
