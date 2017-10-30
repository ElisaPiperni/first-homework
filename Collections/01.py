#collections.Counter()

import collections

ns = input()
shoes_sizes = map(int, raw_input().split())
nc = input()
shoes = collections.Counter(shoes_sizes)

c = 0
for i in range(int(nc)):
    size, price = map(int, raw_input().split())
    if shoes[size] > 0:
        c += price
        shoes.subtract([size])
print c
