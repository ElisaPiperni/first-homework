#Collections.deque()

from collections import deque

n = int(raw_input())
d = deque()

for _ in range(n):
    line = raw_input().split()
    cmd = line[0]
    arg = line[1:]
    cmd += '(' + "".join(arg) + ')'
    eval ("d." + cmd)

for i in d:
    print i,