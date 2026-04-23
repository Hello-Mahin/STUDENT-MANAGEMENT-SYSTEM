import json

FILE = "students.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    branch = input("Enter Branch: ")

    students = load_data()
    students.append({"name": name, "roll": roll, "branch": branch})
    save_data(students)

    print("Student Added Successfully!")

def view_students():
    students = load_data()
    for s in students:
        print(s)

def delete_student():
    roll = input("Enter Roll No to delete: ")
    students = load_data()
    students = [s for s in students if s["roll"] != roll]
    save_data(students)
    print("Deleted Successfully!")

while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice")