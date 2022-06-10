# for i in range(1,51,3):
#     print(i)

def decrement_list(nums):
    # for j in range(0,len(nums)):
    #     print(nums[j])
    for j in range(len(nums)-1, -1, -1):
        print(nums[j])

decrement_list([50,78,65,25,67])