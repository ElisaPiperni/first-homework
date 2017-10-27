#Finding the percentage

if __name__ == '__main__':
    n = int(raw_input())
    students_marks = {}

    for _ in range(n):
        student = raw_input().split()
        name, marks = student[0], map(float, student[1:])
        students_marks[name] = marks

    name = raw_input()
    average = sum(students_marks[name]) / 3
    print
    "%0.02f" % average