n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

numberOfSwaps = 0
for i in xrange(n):
    for j in xrange(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1
    if numberOfSwaps == 0:
        break

print "Array is sorted in {} swaps.".format(numberOfSwaps)
print "First Element: {}".format(a[0])
print "Last Element: {}".format(a[-1])
