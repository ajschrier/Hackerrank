from math import sqrt, floor, ceil

count = int(raw_input())
cases = []

for i in range(0, count):
    inputList = raw_input().split(" ")
    intList = []
    for j in inputList:
        intList.append(int(j))
    cases.append(intList)

for case in cases:
    print int(floor(sqrt(case[1])) - ceil(sqrt(case[0])) + 1)
