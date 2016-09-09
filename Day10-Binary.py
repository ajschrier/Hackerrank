while True:
    input = raw_input()
    try:
        x = int(input)
    except Exception, e:
        if input == 'q':
            break
        print "Try that again."
        continue
    print bin(x)
