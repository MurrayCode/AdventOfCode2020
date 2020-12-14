import math


d = open('input.csv').read().splitlines()
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def check(data, slope):
    isTree = 0
    slopex, slopey = (0, 0)
    while slopey < len(data):
        if data[slopey][slopex % len(data[0])] == '#':
            isTree += 1
        slopex += slope[0]
        slopey += slope[1]
    return isTree

def checktwo(data, slopes):
    return math.prod(check(data, slope) for slope in slopes)



print(check(d, slopes[1]))
print(checktwo(d, slopes))

