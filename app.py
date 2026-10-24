# Student Performance Report System

# Fixed grade categories using tuple
GRADE_CATEGORIES = ("A", "B", "C", "D", "F")


# Function to classify grades
def classify_grade(score):
    if score >= 90:
        return GRADE_CATEGORIES[0]  # A
    elif score >= 80:
        return GRADE_CATEGORIES[1]  # B
    elif score >= 70:
        return GRADE_CATEGORIES[2]  # C
    elif score >= 60:
        return GRADE_CATEGORIES[3]  # D
    else:
        return GRADE_CATEGORIES[4]  # F


# Function to calculate average score
def calculate_average(students):
    total = 0

    for student in students:
        total += student["score"]

    return total / len(students)


# Function to count passing students
def count_passing_students(students):
    count = 0

    for student in students:
        if student["score"] >= 60:
            count += 1

    return count


# List of dictionaries to store student records
students = []

# Accept data for at least five students
for i in range(5):
    print(f"\nEnter information for student {i + 1}")

    name = input("Enter name: ")

    while True:
        try:
            age = int(input("Enter age: "))
            if age > 0:
                break
            print("Age must be greater than 0.")
        except ValueError:
            print("Please enter a valid age.")

    while True:
        try:
            study_hours = float(input("Enter study hours: "))
            if study_hours >= 0:
                break
            print("Study hours cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            score = float(input("Enter Python score (0-100): "))

            if 0 <= score <= 100:
                break
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid score.")

    # Store student information in a dictionary
    student = {
        "name": name,
        "age": age,
        "study_hours": study_hours,
        "score": score,
        "grade": classify_grade(score)
    }

    students.append(student)


# Display complete performance report
print("\n========== STUDENT PERFORMANCE REPORT ==========")

for student in students:
    print(f"\nName: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Study Hours: {student['study_hours']}")
    print(f"Python Score: {student['score']}")
    print(f"Grade: {student['grade']}")

average = calculate_average(students)
passing = count_passing_students(students)

print("\n=============== SUMMARY REPORT ===============")
print(f"Total Students: {len(students)}")
print(f"Average Score: {average:.2f}")
print(f"Passing Students: {passing}")
print(f"Failing Students: {len(students) - passing}")
print("Grade Categories:", GRADE_CATEGORIES)
print("================================================")