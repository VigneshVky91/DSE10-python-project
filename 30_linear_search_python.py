# def l_search(nums_list, search_no):
#     for element in nums_list:
#         if element == search_no:
#             return nums_list.index(element)+1
#     else:
#         return -1

def l_search(nums_list, search_no):
    for index in range(0, len(nums_list)):
        if nums_list[index] == search_no:
            return index+1
    else:
        return -1

my_list = [50,25,65,91,67,87]
sno = int(input("Input the element to be found from the list:"))
element_position = l_search(my_list, sno)

# == is called the comparison operator and returns true or false based on the mathing expression
# = is called assignment operator, this will assign the value at the right side to the variable at the left side
if element_position == -1:
    print("Element not found in the list")
else:
    print(f"Element found at: {element_position}")