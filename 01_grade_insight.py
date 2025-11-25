# Global dictionary to store student names as keys and their marks as values
students = {}


def collect_students_data():
    """
    Continuously prompt the user to enter student names and their marks
    until the user types 'done'. Validates inputs and prevents duplicate names.
    Returns the populated students dictionary.
    """
    while True:
        # Prompt for student name; 'done' exits the loop
        name = input("Enter student name (or 'done' to finish): ")

        if name.lower() == "done":
            break
        # Check if the student has already been entered
        if name in students:
            print("Student already exists.")
            continue

        try:
            # Prompt for marks and convert to float
            marks = float(input(f"Enter the marks for {name}: "))
            students[name] = marks

        except ValueError:
            # Handle non-numeric marks input
            print("Invalid input. Please enter a valid marks.")
            continue

    return students


def display_students_report(students):
    """
    Display a summary report of all students including:
    total count, average, highest, and lowest marks,
    plus a detailed list of each student and their score.
    """
    # Guard clause: do nothing if no data
    if not students:
        print("No students data available.")
        return

    # Extract all marks into a list for easy calculation
    marks = list(students.values())
    highest_marks = max(marks)
    lowest_marks = min(marks)
    average_marks = sum(marks) / len(marks)

    # Find all students who achieved the highest and lowest marks
    topper = [name for name, score in students.items() if score == highest_marks]
    lower = [name for name, score in students.items() if score == lowest_marks]

    # Print formatted report header and summary statistics
    print("-" * 50)
    print(" Student Report Card 📇 ")
    print(f"Total Number of Students: {len(students)}")
    print(f"Average Marks of Students: {average_marks:.2f}")
    print(f"Highest Marks: {highest_marks:.2f} by {', '.join(topper)}")
    print(f"Lowest Marks: {lowest_marks:.2f} by {', '.join(lower)}")
    print("-" * 50)
    print("Detailed Student Report: ")
    # Iterate through each student and print their score
    for name, score in students.items():
        print(f" - {name} : {score:.2f}")
    print("-" * 50)
    print("End of Report.")


# Main execution: collect data first, then display the report
students = collect_students_data()
display_students_report(students)
