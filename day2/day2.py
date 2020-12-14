import csv
import functools
import operator

with open('input.csv')as f:
    reader = csv.reader(f, delimiter='\n')
    input = list(reader)
    merged = functools.reduce(operator.iconcat, input, [])

def check(list):
    validcount = 0
    for pwcheck in merged:
        split = pwcheck.split()
        nums = split[0].split("-")
        first = int(nums[0])
        second = int(nums[1])
        letter = str(split[1].replace(':', ''))
        count = 0
        pw = split[2]
        for i in pw:
            if i == letter:
                count += 1
        if count >= first and count <=second:
            validcount +=1  
        
    return print(validcount)

check(merged)