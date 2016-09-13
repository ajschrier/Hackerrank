length = int(raw_input())
inputList = raw_input().split(" ")
outputList = []

for i in range(0, len(inputList)):
    outputList.append(inputList.pop())

outputString = ""
for i in outputList:
    outputString += i
    outputString += " "

print outputString.strip()
