#Nested Lists

students = []
n = int(raw_input())
for _ in range(n):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])

s = sorted(students, key=lambda x: (x[1], x[0]))

lowest = s[0][1]
for _ in range(n):
    if s[0][1] == lowest:
        s.remove(s[0])

sec_low = s[0][1]
for i in range(len(s)):
    if s[i][1] == sec_low:
        print s[i][0]
