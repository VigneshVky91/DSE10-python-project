myTuple = (20,30,45, 45, 45,54,54,65)
myList = [50,78,65,89,98]


print("Tuple elements: ",myTuple)
print("Length of Tuple: ", len(myTuple))

print(f"The index of 45: {myTuple.index(45)}")

print("Tuple elements: ",myTuple)
print(f"The total occurrences in the tuple are : {myTuple.count(54)}")
print(f"The maximum element in the tuple is : {max(myTuple)}")
print(f"The minimum element in the tuple is : {min(myTuple)}")

myTuple2 = tuple(myList)
myList2 = list(myTuple)

print(type(myTuple2))
print(type(myList2))