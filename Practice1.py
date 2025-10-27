def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"
    
def generate_student_report(name,score):
    grade = calculate_grade(score)
    print(f"{name} has scored {score} marks and get grade '{grade}'")

generate_student_report("sam",99)