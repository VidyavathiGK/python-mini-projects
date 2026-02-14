import os

FILE_NAME = "students.txt"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(roll + "," + name + "," + marks + "\n")

    print("Student added successfully!\n")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

        if not data:
            print("No records found.\n")
            return

        print("\n--- Student Records ---")
        for line in data:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Marks: {marks}")
        print()


def search_student():
    roll_search = input("Enter Roll Number to search: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        found = False
        for line in file:
            roll, name, marks = line.strip().split(",")
            if roll == roll_search:
                print(f"Found -> Name: {name}, Marks: {marks}\n")
                found = True
                break

        if not found:
            print("Student not found.\n")


def delete_student():
    roll_delete = input("Enter Roll Number to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    lines = []
    deleted = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            roll, name, marks = line.strip().split(",")
            if roll != roll_delete:
                file.write(line)
            else:
                deleted = True

    if deleted:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

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
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
