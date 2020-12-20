command = input()
courses = {}
while not command == 'end':
    course, name = command.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(name)
    command = input()
courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))
for key, value in courses.items():
    value.sort()
for key, value in courses.items():
    print(f'{key}: {len(value)}')
    for el in value:
        print(f'-- {el}')