#Alphabet Rangoli

import string

def print_rangoli(size):
    n = 1 + (int(size)-1)*4
    alpha = list(string.ascii_lowercase)
    L = []
    for i in range(size-1, -1, -1):
        s = '-'.join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(n, "-"))
    print('\n'.join(L+L[-2::-1]))