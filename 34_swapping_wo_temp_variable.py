a = 100
b = 200

print("Before swapping:")
print(f"a = {a}")
print(f"b = {b}")

# Logic_to_swap

a = a+b
# a = 100+200 ===> 300 will be stored to a
b = a-b
# b = 300-200 ===> 100 will be now stored into b
a = a-b
# a = 300-100 ===> 200 will be now stored into a

print("After swapping:")
print(f"a = {a}")
print(f"b = {b}")
