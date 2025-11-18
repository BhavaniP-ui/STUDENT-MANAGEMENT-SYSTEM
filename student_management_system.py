import csv

# ------------------------------
# Student Management System
# ------------------------------

FILE = "students.csv"

# Initialize file if not present
def initialize_file():
    try:
        with open(FILE, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll No", "Name", "Department", "Marks"])
    except FileExistsError:
        pass

# Add a student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    marks = input("Enter Marks: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, dept, marks])

    print("Student added successfully!")

# View all students
def view_students():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# Search a student by roll number
def search_student():
    roll = input("Enter Roll No to search: ")
    found = False

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == roll:
                print("Student Found:", row)
                found = True
                break
    
    if not found:
        print("Student not found.")

# Delete a student
def delete_student():
    roll = input("Enter Roll No to delete: ")
    rows = []

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] != roll:
                rows.append(row)

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Record deleted successfully (if existed).")

# Main Menu
def menu():
    print("\n---- Student Management System ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice

# Main Program
initialize_file()

while True:
    choice = menu()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
