GRADE_POINTS = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "C": 2.0
}

def calculate_gpa(grades):
    total = 0
    for grade in grades:
        total += GRADE_POINTS.get(grade.upper(), 0)
    
    return round(total / len(grades), 2)