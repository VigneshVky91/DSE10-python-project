def bubble_sort(nums):
    for i in range (0, len(nums)-1):
        for j in range(0, len(nums)-(i+1)):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]

nums_list = [80,8,78,96,69,86,100]
print("Before sorting: ")
print(nums_list)

bubble_sort(nums_list)

print("After sorting: ")
print(nums_list)