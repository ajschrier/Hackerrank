inputCount = int(raw_input())
inputDict = [raw_input().split() for _ in range(inputCount)]
phoneBook = {k: v for k, v in inputDict}

while True:
    try:
        name = raw_input()
        if name in phoneBook:
            print ("{}={}").format(name, phoneBook[name])
        else:
            print("Not found")
    except:
        break
