def longest_streaks(daily_records):
    if not daily_records:
        return {}
    all_students = set()
    for day in daily_records:
        all_students.update(day.keys())
    streaks = {student: [0, 0] for student in all_students}

    for day in daily_records:
        for student in all_students:
            if day.get(student) == 'present':
                streaks[student][0] += 1
                streaks[student][1] = max(streaks[student][1], streaks[student][0])
            else:
                streaks[student][0] = 0
    return {student: info[1] for student, info in streaks.items()}

print(longest_streaks([
    {"Ada": "present"}, 
    {"Ada": "present"},
    {"Ada": "absent"},
    {"Ada": "present"}
    ]))