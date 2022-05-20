number = int(input("Input a number: "))  # 54321 ---> 12345
i = 0
num_str = ""

while number>0:
    print(number)
    i = int(number %10)
    number = number//10
    num_str+=str(i)

print(num_str)