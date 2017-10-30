#Collections.namedtuple()

from collections import namedtuple

n_students = int(raw_input())
title = ",".join(raw_input().split())

Student = namedtuple('Student', title)

count = 0
for _ in range(n_students):
    a, b, c, d = raw_input().split()
    t = Student(a, b, c, d)
    count += float(t.MARKS)
average = count/n_students
print "%0.02f" %average