from math import sqrt
import timeit

start_time = timeit.default_timer()
maxEuclideanLength = 0
# for iteration in xrange(1000000):
count = 9
inputGrid = ["*********",
             "****.****",
             "**.....**",
             "**.....**",
             "*.......*",
             "**.....**",
             "**.....**",
             "****.****",
             "*********"]

grid = []
for i in xrange(count):
    row = []
    for j in inputGrid[i]:
        if j == "*":
            row.append(0)
        elif j == ".":
            row.append(1)
    grid.append(row)

# Eliminate obscured cells
cases = []
for i in xrange(count):
    if i == 0 or i == count-1:
        continue
    for j in xrange(count):
        if j == 0 or j == count-1:
            continue
        elif bool(grid[i][j]):
            cases.append((i, j))

for testCase in cases:
    lengths = []
    p1 = testCase[0]
    p2 = testCase[1]
    for destinationCase in cases:
        if destinationCase == testCase:
            continue
        q1 = destinationCase[0]
        q2 = destinationCase[1]
        lengths.append(sqrt(((q1-p1)**2))+((q2-p2)**2))
    if min(lengths) > maxEuclideanLength:
        maxEuclideanLength = min(lengths)

print int(maxEuclideanLength)
print "Completion time {} seconds".format(timeit.default_timer() - start_time)
