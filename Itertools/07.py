#Maximize It!

from itertools import product

K, M = map(int,raw_input().split())
l =[]
for _ in range(K):
    line = map(int,raw_input().split())
    n = line[0]
    lst = line[1:]
    sqr = list(lst[i]**2 for i in range(n))
    l.append(sqr)
prod = list(product(*l))
s = list(sum(x) for x in prod)
mod = list(x%M for x in s)
ma = max(mod)
print ma