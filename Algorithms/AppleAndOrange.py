#!/bin/python


def appleAndOrange():
    pass

if __name__ == '__main__':
    s, t = raw_input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = raw_input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = raw_input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = map(int, raw_input().strip().split(' '))
    orange = map(int, raw_input().strip().split(' '))
