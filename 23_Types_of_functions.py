#Functions without arguments and without return values (default function)
def defaultFunction():
    print("Hello I am a function with no arguments and return values")
    print("I will do whatever the task you ask me to do but won't respond you back with a return value!")

#Function with argument and without return values

def functionWithTwoArgsButNoReturnValue(name, no_of_times):
    for i in range(0, no_of_times):
        print(name)
    print("I am a function with two parameters and no return value")

#Function without argument and with return values
def functionWithNoArgsButReturnValue():
    print("I am a function without any arguments but I will return you a greeting message")
    print("Make sure to store the result on a local variable")
    return "Have a great day ahead!!!"

#Function with argument and with return values
def functionWithTwoArgsAndReturnValue(num1, num2):
    print("I am a function with two arguments and I will return the result!!!")
    sum = num1+num2
    return f"Sum = {num1+num2}"

# defaultFunction()
# functionWithTwoArgsButNoReturnValue("Puthearin", 5)
# messageFromFunction = functionWithNoArgsButReturnValue()
# print(messageFromFunction)
resultFromFunction = functionWithTwoArgsAndReturnValue(45,65)
print(resultFromFunction)