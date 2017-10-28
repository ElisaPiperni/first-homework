#Compress the String!

from itertools import groupby

data = groupby(raw_input())

for key, value in data:
    character = key
    occurrences = len(list(value))

    print "(" + str(occurrences) + ", " + str(character) + ")",