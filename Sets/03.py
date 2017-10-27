#No Idea!

n,m = raw_input().split()
arr = map(int,raw_input().split())
A = set(map(int,raw_input().split()))
B = set(map(int,raw_input().split()))
hap = 0

for i in arr:
    if i in A:
        hap += 1
    elif i in B:
        hap -= 1
print hap