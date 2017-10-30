#Most Common

#!/bin/python

import sys
from collections import Counter

if __name__ == "__main__":
    s = raw_input().strip()
    c = Counter(s)
    sort = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    for i in range(0,3):
        print sort[i][0], sort[i][1]