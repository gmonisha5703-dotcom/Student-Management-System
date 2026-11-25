students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    students[roll] = {"name": name, "age": age}
    print("Student Added Successfully!")

def view_students():
    for roll, details in students.items():
        print(roll, details)

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid Choice")

main()
