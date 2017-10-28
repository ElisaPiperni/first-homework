#itertools.permutations()

from itertools import permutations

S,k = raw_input().split()
l = list(permutations(sorted(S),int(k)))
perm = []
for i in l:
    perm.append(''.join(i))

print "\n".join(map(str,perm))