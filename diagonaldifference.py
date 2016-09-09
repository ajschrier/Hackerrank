# coding: utf-8
n = int(raw_input())
a = []
for i in range(n):
    b = raw_input().split()
    c = [int(x) for x in b]
    a.append(c)

d1 = 0
d2 = 0
for i in range(n):
    d1 += a[i][i]
    d2 += a[i][n-i-1]

print abs(d1 - d2)

