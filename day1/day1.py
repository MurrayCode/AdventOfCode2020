
numbers = ['1721', '979', '366', '299', '675', '1456']

def sum(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j+1 <= len(nums):
                if int(nums[i]) + int(nums[j+1]) == 2020:
                    print(nums[i] + " + " + nums[j+1] + " = 2020")
                    return print(int(nums[i]) * int(nums[j+1]))
                else:
                    print("does not equal 2020")



sum(numbers)