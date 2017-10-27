#String Validators

if __name__ == '__main__':
    s = raw_input()

    a = False
    for i in s:
        if i.isalnum():
            a = True
    print a

    b = False
    for i in s:
        if i.isalpha():
            b = True
    print b

    c = False
    for i in s:
        if i.isdigit():
            c = True
    print c

    d = False
    for i in s:
        if i.islower():
            d = True
    print d

    e = False
    for i in s:
        if i.isupper():
            e = True
    print e
