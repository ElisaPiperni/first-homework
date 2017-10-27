#Lists

if __name__ == '__main__':
    N = int(raw_input())
    lst = []
for _ in range (N):
    line = raw_input().split()
    cmd = line[0]
    arg = line[1:]
    if line[0] == 'print':
        print lst
    else:
        cmd += '(' + ",".join(arg) + ')'
        eval ("lst." + cmd)
