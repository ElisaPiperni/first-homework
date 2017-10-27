#sWAP cASE

def swap_case(s):
    s_swap = ''
    for i in s:
        if i.islower():
            s_swap += i.upper()
        else:
            s_swap += i.lower()
    return s_swap