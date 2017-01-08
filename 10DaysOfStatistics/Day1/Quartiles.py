def listMidpoint(lst):
    mid = len(lst) / 2
    if len(lst) % 2 is 0:
        return (lst[mid] + lst[mid - 1]) / 2
    else:
        return lst[mid]


def quartiles(count, lst):
    lst.sort()
    q2 = listMidpoint(lst)
    mid = len(lst) / 2
    if len(lst) % 2 is 0:
        q1 = listMidpoint(lst[:mid])
        q3 = listMidpoint(lst[mid:])
    else:
        q1 = listMidpoint(lst[:mid])
        q3 = listMidpoint(lst[mid + 1:])
    return [q1, q2, q3]


def main():
    results = quartiles(int(raw_input()),
                        [int(x) for x in raw_input().split()])
    for i in results:
        print i


if __name__ == '__main__':
    main()
