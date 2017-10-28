#Iterables and Iterators

from itertools import combinations

n = int(raw_input())
lst = raw_input().split()
k = int(raw_input())

ind_a = []
for i in range(len(lst)):
    if lst[i] == 'a':
        ind_a.append(i+1)

indices = list(range(1, n+1))
comb_i = list(combinations(indices, k))

count = 0
for c in comb_i:
    for i in ind_a:
        if i in c:
            count +=1
            break

prob =count/float(len(comb_i))
print prob
