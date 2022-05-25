def sayHello():
    print("Hello world...")

def sayHello10Times():
    # print("Hello world\n"*10)
    for i in range(0,10):
        print("Hello world")

def addTwoNumbers():
    num1 = int(input("Input the first number"))
    num2 = int(input("Input the second number"))
    print(f"Sum = ${num1+num2}")

def subtractTwoNumbers():
    num1 = int(input("Input the first number"))
    num2 = int(input("Input the second number"))
    print("Difference = ", (num1 - num2))

def multiplyTwoNumbers():
    num1 = int(input("Input the first number"))
    num2 = int(input("Input the second number"))
    print("Product = ", (num1 * num2))

def divTwoNumbersFindQuotient():
    num1 = int(input("Input the first number"))
    num2 = int(input("Input the second number"))
    print("Quotient = ", (num1 // num2))

def divTwoNumbersFindRemainder():
    num1 = int(input("Input the first number"))
    num2 = int(input("Input the second number"))
    print("Remainder = ", (num1 % num2))
# sayHello10Times()

choice = int(input("Input your choice of operations\n1. Addition\n2. Subtraction\n3. Multiplication"
                   "\n4. Division(Quotient)\n5. Division(Remainder)\n"))

if choice==1:
    addTwoNumbers()
elif choice==2:
    subtractTwoNumbers()
elif choice==3:
    multiplyTwoNumbers()
elif choice==4:
    divTwoNumbersFindQuotient()
elif choice==5:
    divTwoNumbersFindRemainder()

