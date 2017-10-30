#Word Order

from collections import OrderedDict, Counter

n = int(raw_input())
words = []
d = OrderedDict()
for _ in range(n):
    words.append(raw_input())
c = Counter(words)
for w in words:
    d[w] = c[w]

print len(d)
for v in d.values():
    print v,