#DefaultDict Tutorial

from collections import defaultdict

na, nb = map(int, raw_input().split())
a = defaultdict(list)
b = []

for i in range(1, na+1):
    a[raw_input()].append(i)

for _ in range(nb):
    b.append(raw_input())

for word in b:
    if word in a:
        print " ".join(map(str,(a[word])))
    else:
        print -1