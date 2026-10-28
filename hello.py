
def analyze_marks(marks):
    if not marks:
        raise ValueError("Marks cannot be empty")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")

    average = sum(marks) / len(marks)
    result = "Pass" if average >= 40 else "Fail"

    return average, result


if __name__ == "__main__":
    student_marks = [75, 80, 65]

    average, result = analyze_marks(student_marks)

    print("Student Marks Analyzer")
    print("Marks:", student_marks)
    print("Average:", average)
    print("Result:", result)
