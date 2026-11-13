# Create a menu-driven student marks management program using a tuple for
# subjects, a set for unique student names, and a dictionary containing
# students' marks in lists. Define functions to add students, display records,
# and calculate averages. Use recursion to calculate total marks and handle
# ValueError, ZeroDivisionError, TypeError, and NameError exceptions.




# Store subject names in a tuple
subjects = ("Math", "Science", "English")

# Store unique student names in a set
student_names = set()

# Store student marks in a dictionary
students = {}


# Recursive function to calculate total marks
def calculate_total(marks):
    if not isinstance(marks, list):
        raise TypeError

    if len(marks) == 0:
        return 0

    if not isinstance(marks[0], (int, float)):
        raise TypeError

    return marks[0] + calculate_total(marks[1:])


# Function to add a student
def add_student():
    name = input("Enter student name: ")

    if name in student_names:
        print("Student already exists.")
        return

    marks = []

    try:
        for subject in subjects:
            mark = int(input("Enter marks for " + subject + ": "))
            marks.append(mark)

        students[name] = marks
        student_names.add(name)

        print("Student added successfully.")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")


# Function to display all student records
def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for name, marks in students.items():
            print(name, ":", marks)


# Function to calculate average marks
def calculate_average():
    name = input("Enter student name to calculate average: ")

    try:
        if name not in students:
            raise NameError

        marks = students[name]
        total = calculate_total(marks)

        if len(marks) == 0:
            raise ZeroDivisionError

        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Student name not found.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except TypeError:
        print("Marks data type error.")

# Main menu
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            calculate_average()

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter 1 to 4.")

    except ValueError:
        print("Please enter a valid menu number.")
