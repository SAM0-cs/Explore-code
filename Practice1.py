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
    

def generate_student_report(names,score):
    grade = calculate_grade(score)
    return f"{names.upper()} has scored {score} and get grade {grade}"

print(generate_student_report("akya",90))
print()

students = ['sam','aditi','ram','tejya','abhi']
marks = [99,89,56,35,70]

result = []
for i in range(len(students)):
    msg = generate_student_report(students[i],marks[i])
    result.append(msg)

for i in result:
    print(i)
    print()


