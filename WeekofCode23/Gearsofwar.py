count = int(raw_input())
testcases = []
for i in xrange(count):
    testcases.append(int(raw_input()))

for case in testcases:
    if case % 2 == 0:
        print "Yes"
    else:
        print "No"
