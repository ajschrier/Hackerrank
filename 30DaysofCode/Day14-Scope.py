# Provided
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Beginning of exercise
    def computeDifference(self):
        maxDiff = 0
        for i in xrange(len(self.__elements)-1):
            for j in xrange(len(self.__elements[i+1:])):
                x = abs(a[i]-a[i+1:][j])
                if x > maxDiff:
                    maxDiff = x
        self.maximumDifference = maxDiff
    # End of exercise
_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
