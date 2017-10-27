#Set Mutations

na = int(raw_input())
A = set(map(int, raw_input().split()))
ns = int(raw_input())

for _ in range(ns):
    operation, length = raw_input().split()
    S = str(set(map(int, raw_input().split())))
    operation += "(" + S + ")"
    eval("A." + operation)

print
sum(A)
