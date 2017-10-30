#Collections.OrderedDict()

from collections import OrderedDict

n = int(raw_input())
dic_items = OrderedDict()
for _ in range(n):
    l = raw_input().split()
    item_name = " ".join(l[:-1])
    price = int(l[-1])
    if item_name in dic_items:
        dic_items[item_name] += price
    else:
        dic_items[item_name] = price

for i, p in dic_items.items():
    print i, p