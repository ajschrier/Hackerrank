input = raw_input()
x = int(input)
binaryString = bin(x)[2:]
currentLength = 0
maxLength = 0
for i in binaryString:
    if i == '1':
        currentLength += 1
    else:
        if currentLength > maxLength:
                maxLength = currentLength
        currentLength = 0
if currentLength > maxLength:
    maxLength = currentLength
print maxLength
