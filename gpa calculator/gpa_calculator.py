# compute the gpa of a student with 6 courses

courses = []
num_courses = 0
total_units = 0
total_weighted_score = 0


while num_courses < 6:
    course = input("Enter the course: ")
    unit = int(input("Enter the course credit unit(0-6): "))
    grade = input("Enter your grade(A-F): ").upper()

    while grade not in ["A", "B", "C", "D", "F"]:
        print("Invalid Grade")
        grade = input("Enter your grade(A-F): ").upper()


    if grade == "A":
        weighted_score = 5 * unit
    elif grade == "B":
        weighted_score = 4 * unit
    elif grade == "C":
        weighted_score = 3 * unit
    elif grade == "D":
        weighted_score = 2 * unit
    elif grade == "F":
        weighted_score = 0 * unit
    else:
        print("Invalid Grade")
        grade = input("Enter your grade(A-F): ")

    total_weighted_score += weighted_score
    total_units += unit

    courses.append(course)
    num_courses += 1

    print(f"COURSE: {course}:,"
          f" UNIT: {unit}, "
          f" GRADE: {grade}, "
          f"WEIGHTED SCORE: {weighted_score}\n")


gpa = total_weighted_score / total_units

print(f"TOTAL WEIGHTED SCORE = {total_weighted_score}")
print(f"TOTAL UNITS = {total_units}")
print(f"GPA: {gpa}")
