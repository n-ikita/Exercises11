from solution import Subject, FacultySchedule

with open('subjects.txt', encoding='utf8') as file:
    subjects = file.readlines()

faculty_schedule = FacultySchedule()
for line in subjects:
    name, group, number, teacher = line.split()
    group = int(group)
    number = int(number)
    faculty_schedule.add_subject(Subject(name, group, number, teacher))

faculty_schedule.print_group_schedule(22704)
