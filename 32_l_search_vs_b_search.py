def l_search(nums_list, search_no):
    index = 0
    counter = 0
    while index < len(nums_list):
        counter+=1
        if nums_list[index] == search_no:
            return index+1, counter
        index+=1
    return -1,counter

def b_search(nums_list, sno):
    counter = 0
    beg = 0
    end = len(nums_list) - 1
    while beg<end:
        counter+=1
        mid = (beg+end)//2
        if nums_list[mid]==sno:
            return mid,counter
        elif nums_list[mid]>sno:
            end = mid-1
        else:
            beg = mid+1
    else:
        return -1,counter


nums_list = []
for i in range(0, 10000000):
    nums_list.insert(i, i+1)
sno = 9999999

pos, counter = b_search(nums_list, sno)
message = "Element Not found in the list"
if pos !=-1:
    message = f"Element found at position : {pos+1}"
    print(f"It took {counter} no of iterations to find the element for b search:")
print(message)

pos, counter = l_search(nums_list, sno)
message = "Element Not found in the list"
if pos !=-1:
    message = f"Element found at position : {pos+1}"
    print(f"It took {counter} no of iterations to find the element for l search:")
print(message)