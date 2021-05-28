n = int(input())

students = {}

for _ in range(n):
    line = tuple(input().split())
    student, grade = line
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grade in students.items():
    grades = ['{:.2f}'.format(x) for x in grade]
    print(f"{student} -> {' '.join(grades)} (avg: {sum(grade)/ len(grade):.2f})")
