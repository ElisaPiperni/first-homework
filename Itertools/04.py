#itertools.combinations_with_replacement()

from itertools import combinations_with_replacement

S, k = raw_input().split()
l = list(combinations_with_replacement(sorted(S), int(k)))
comb = []
for i in l:
    comb.append(''.join(i))

print "\n".join(map(str,comb))