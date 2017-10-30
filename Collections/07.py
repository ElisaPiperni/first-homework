#Piling Up!

tests = int(raw_input())
for _ in range(tests):
    n = int(raw_input())
    lenghts = map(int, raw_input().split())
    ind_min = lenghts.index(min(lenghts))
    if lenghts[0:ind_min] == sorted(lenghts[0:ind_min], reverse = True) and lenghts[ind_min:] == sorted(lenghts[ind_min:]):
        print 'Yes'
    else:
        print 'No'