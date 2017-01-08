def mean(dataset):
    x = 0
    for i in dataset:
        x += i
    return round(float(x)/len(dataset), 1)


def median(dataset, n):
    dataset.sort()
    if n % 2 is 0:
        return (dataset[n/2 - 1] + dataset[n/2]) / 2.0
    else:
        return dataset[n/2 - 1]


def mode(dataset):
    dataset.sort()
    a = {}
    for i in dataset:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    return max(dataset, key=dataset.count)


def main():
    n = int(raw_input())
    s = [int(x) for x in raw_input().split()]
    print mean(s)
    print median(s, n)
    print mode(s)

if __name__ == '__main__':
    main()
