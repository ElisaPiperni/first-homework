#Set .discard(), .remove() & .pop()

n = input()
s = set(map(int, raw_input().split()))
n_cmd = input()

for _ in range(n_cmd):
    r = raw_input().split()
    cmd = r[0]
    arg = r[1:]
    cmd += '(' + "".join(arg) + ')'
    eval ("s." + cmd)
print sum(s)