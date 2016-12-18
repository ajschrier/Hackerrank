#!/bin/python
import string


def pdfSelection(h, word):
    heights = {}
    for i in xrange(26):
        heights[string.lowercase[i]] = h[i]
    width = 0
    for letter in word:
        if int(heights[letter]) > width:
            width = int(heights[letter])
    return width * len(word)


if __name__ == '__main__':
    h = map(int, raw_input().strip().split(' '))
    word = raw_input().strip()
    print pdfSelection(h, word)
