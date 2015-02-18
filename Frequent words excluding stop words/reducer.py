#!/usr/bin/env python

from operator import itemgetter
import sys
from collections import defaultdict

current_word = None
current_count = 0
word = None
cache = defaultdict(int)

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    cache[word] = count
    current_count += count

n = 100
for key, value in sorted(cache.iteritems(),key=lambda (k,v): (v,k),reverse=True):
    print '%s\t%s' % (key, str(float(value)/current_count))
    n -= 1
    if n == 0:
	break
