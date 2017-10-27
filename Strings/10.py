#String Formatting

def print_formatted(number):
    space = len(bin(number)[2:])
    for i in range(1, number + 1):
        o = oct(i)[1:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]

        print str(i).rjust(space) + o.rjust(space + 1) + h.rjust(space + 1) + b.rjust(space + 1)