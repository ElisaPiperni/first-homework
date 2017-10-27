#Symmetric Difference

input()
lst_a = list(map(int, raw_input().split()))
input()
lst_b = list(map(int, raw_input().split()))

a = set(lst_a)
b = set(lst_b)

sd = sorted(a ^ b)
for n in sd:
    print n

