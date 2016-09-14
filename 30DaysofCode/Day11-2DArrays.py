import sys

matrix = []
for i in xrange(6):
    matrix.append([int(i) for i in raw_input().split()])
rows = [(i, i+1, i+2) for i in xrange(4)]

maxTotal = -sys.maxint - 1

for i in xrange(4):
    for row in rows:
        total = int(matrix[i][row[0]]) + \
                int(matrix[i][row[1]]) + \
                int(matrix[i][row[2]]) + \
                int(matrix[i+1][row[1]]) + \
                int(matrix[i+2][row[0]]) + \
                int(matrix[i+2][row[1]]) + \
                int(matrix[i+2][row[2]])
        if total > maxTotal:
            maxTotal = total

print maxTotal
