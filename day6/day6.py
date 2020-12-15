import csv
import functools
import operator
from collections import *
import math

data = open("input.csv", "r")
groups = data.read().split("\n\n")

def check():
    count = 0
    for group in groups:
        x = Counter(group)
        count +=len(x)
        if '\n' in x:
            count -= 1
    return count


def checktwo():
    count = 0
    for group in groups:
        y = len(group.split())
        x = Counter(group)
        count += sum(v == y for _, v in x.items())
        if x['\n'] == y:
            count -= 1
    return count

print(check())
print(checktwo())