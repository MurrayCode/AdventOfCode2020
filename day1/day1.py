import csv
import functools
import operator

numbers = ['1721', '979', '366', '299', '675', '1456']
with open('input.csv')as f:
    reader = csv.reader(f, delimiter='\n')
    input = list(reader)
    merged = functools.reduce(operator.iconcat, input, [])

def sum(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
                if int(nums[i]) + int(nums[j]) == 2020:
                    print(nums[i] + " + " + nums[j] + " = 2020")
                    return print(int(nums[i]) * int(nums[j]))
                else:
                    print("does not equal 2020")
                    print(j)


def trisum(nums):
    length = len(nums)
    for i in range(length):
        for j in range(length):
            for x in range(length):
                    if int(nums[i]) + int(nums[j]) + int(nums[x]) == 2020:
                        print(nums[i] + " + " + nums[j] + " + " + nums[x] + " = 2020")
                        return print(int(nums[i]) * int(nums[j]) * int(nums[x]))
                    else:
                        print("does not equal 2020")
                        print(j)
                        print(x)
sum(merged)
trisum(merged)