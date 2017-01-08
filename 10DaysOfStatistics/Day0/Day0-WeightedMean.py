n = int(raw_input())
values = [int(x) for x in raw_input().split()]
weights = [int(x) for x in raw_input().split()]

num = 0.0
for i in xrange(n):
    num += (values[i] * weights[i])
den = sum(weights)

print round(num/den, 1)
