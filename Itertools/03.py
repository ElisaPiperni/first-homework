#itertools.combinations()

from itertools import combinations

S, k = raw_input().split()
l = []
for n in range(1, int(k) + 1):
    l.append(list(combinations(sorted(S), n)))
comb = []
for sub_l in l:
    for i in sub_l:
        comb.append(''.join(i))

print "\n".join(map(str, comb))