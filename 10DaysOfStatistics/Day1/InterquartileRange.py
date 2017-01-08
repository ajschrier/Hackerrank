import Quartiles


def interQuartileRange(lst):
        lst.sort()
        mid = len(lst) / 2
        if len(lst) % 2 is 0:
            q1 = Quartiles.listMidpoint(lst[:mid])
            q3 = Quartiles.listMidpoint(lst[mid:])
        else:
            q1 = Quartiles.listMidpoint(lst[:mid])
            q3 = Quartiles.listMidpoint(lst[mid + 1:])
        return float(q3 - q1)


if __name__ == '__main__':
    n = int(raw_input())
    elements = [int(x) for x in raw_input().split()]
    frequency = [int(x) for x in raw_input().split()]
    lst = []
    for i in xrange(n):
        for j in xrange(frequency[i]):
            lst.append(elements[i])
    print interQuartileRange(lst)
