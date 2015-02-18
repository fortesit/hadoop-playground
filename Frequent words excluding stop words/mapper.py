#!/usr/bin/env python

import sys
from collections import defaultdict

cache = defaultdict(int)

filename = 'common-english-words.txt'
fr = open(filename)
string = fr.read()
stop_words = []

for token in string.split(','):
    stop_words.append(token)

for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = ''.join(c for c in line if c.isalpha() or c.isspace()).split()

    for word in words:
        if word in stop_words:
            continue
        cache[word] += 1

for (word, count) in cache.iteritems():
    print '%s\t%s' % (word, count)
