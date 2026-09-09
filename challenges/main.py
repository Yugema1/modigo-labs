def group_by_grade(students):
    grouped_grades = {}
    for student in students:
        name = student['name']
        score = student['score']
        if score < 60:
            grade = 'F'
        elif score < 70:
            grade = 'D'
        elif score < 80:
            grade = 'C'
        elif score < 90:
            grade = 'B'
        else:
            grade = 'A'

        if grade not in grouped_grades:
            grouped_grades[grade] = [name]
        else:
            grouped_grades[grade].append(name)
    return grouped_grades

print(group_by_grade([{"name": "Ada", "score": 95}, {"name": "Bola", "score": 82}]))