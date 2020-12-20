n = int(input())
students = {}
for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)
filtered_students = {}
for student, grades in students.items():
    average_grades = sum(grades) / len(grades)
    if average_grades >= 4.50:
        filtered_students[student] = average_grades
for student, av_grade in sorted(filtered_students.items(), key=lambda x: -x[1]):
    print(f"{student} -> {av_grade:.2f}")