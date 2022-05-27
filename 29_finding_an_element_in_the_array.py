# def finding_an_element_in_array(arr, sno):
#     for i in range(0, len(arr)):
#         if arr[i] == sno:
#             return f"Element found at index {i}"
#     return "Element not found in the array..."

def finding_an_element_in_array(arr, sno):
    for num in arr:
        if num == sno:
            return f"Element found at index {arr.index(num)}"
    return "Element not found in the array..."


result = finding_an_element_in_array([51,45,78,98,56],56)
print(result)