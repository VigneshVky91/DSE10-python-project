number = int(input("Input a number: "))
i = 0
sum = 0

while number>0:
    i = number % 10
    number = number // 10
    sum+=i

print(f"Sum = {sum}")
