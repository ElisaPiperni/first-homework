#The Minion Game

def minion_game(string):
    n = len(string)
    vow = 'AEIOU'
    Stu = 0
    Kev = 0
    for i in range(n):
        score = len(string)-i
        if string[i] in vow:
            Kev += score
        else:
            Stu += score
    if Kev > Stu:
        print 'Kevin ' + str(Kev)
    if Kev < Stu:
        print 'Stuart ' + str(Stu)
    if Kev == Stu:
        print 'Draw'
