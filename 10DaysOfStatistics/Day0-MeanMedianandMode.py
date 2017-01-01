def mean(dataset):
    x = 0
    for i in dataset:
        x += i
    return round(float(x)/len(dataset), 1)


def median(dataset, n):
    x = dataset.sort()
    if len(x) % 2 is not 0:
        return (x[len(x)/2] + x[len(x)/2 - 1])
    else:
        return x[len(x)/2 - 1]


def mode(dataset):
    x = dataset.sort()


def main():
    n = int(raw_input())
    x = [int(x) for x in raw_input().split()]
    print mean(x)
    print median(x, n)


if __name__ == '__main__':
    main()
