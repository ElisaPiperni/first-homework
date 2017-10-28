#itertools.product()

from itertools import product

A = map(int,raw_input().split())
B = map(int,raw_input().split())
pro = list(product(A, B))
print " ".join(map(str,pro))