# Student Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    students[roll] = {"name": name, "age": age}
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No records found.\n")
        return
    for roll, info in students.items():
        print(f"Roll: {roll}, Name: {info['name']}, Age: {info['age']}")
    print()

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        students[roll] = {"name": name, "age": age}
        print("Updated successfully!\n")
    else:
        print("Student not found!\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Deleted successfully!\n")
    else:
        print("Student not found!\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice\n")