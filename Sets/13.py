#Check Strict Superset

A = set(map(int,raw_input().split()))
n = int(raw_input())
l = []
for _ in range(n):
    N = set(map(int,raw_input().split()))
    l.append(A.issuperset(N))
print all(l)