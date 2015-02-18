#!/usr/bin/env python

import sys
from collections import defaultdict

cache = defaultdict(int)

for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = ''.join(c for c in line if c.isalpha() or c.isspace()).split()

    for word in words:
        cache[word] += 1

for (word, count) in cache.iteritems():
    print '%s\t%s' % (word, count)
