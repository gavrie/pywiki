#!/usr/bin/env python

import re
import sys

try:
    progname, pattern = sys.argv
except ValueError:
    print "Usage: {} <pattern>".format(sys.argv[0])
    sys.exit(1)

for line in sys.stdin:
    if re.search(pattern, line):
        print line.strip()
