count = int(raw_input())
strings = []
output = []

for string in range(0, count):
    strings.append(raw_input())

for string in strings:
    even = ""
    odd = ""
    for i in range(0, len(string)):
        if i % 2 == 0:
            even += string[i]
        else:
            odd += string[i]
    output.append("{} {}".format(even, odd))

for string in output:
    print string
