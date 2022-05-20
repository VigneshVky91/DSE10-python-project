num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))

if num1>num2:
    if num1>num3:
        print("Number 1 is the greatest")
    else:
        print("Number 3 is the greatest")

elif num2>num3:
    print("Num2 is the greatest")
else:
    print("Num3 is the greatest")

# else:
#     if num2>num3:
#         print("Num2 is the greatest")
#     else:
#         print("Num3 is the greatest")