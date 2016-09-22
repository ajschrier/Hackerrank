count = int(raw_input())
cases = []

for i in range(0, count):
    input = raw_input()
    cases.append(int(input))


def treeHeight(cycles):
    height = 1
    if cycles == 0:
        return height
    else:
        for cycle in range(cycles):
            if cycle % 2 == 0:
                height *= 2
            else:
                height += 1
        return height

for case in cases:
    print treeHeight(case)
