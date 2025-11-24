student = {}


def add_student():
    print("Add Student")
    reg = input("enter registration number: ")
    if reg in student:
        print("student already exists!")
    else:
        name = input("Enter name: ")
        course = input("Enter course: ")

        cgpa = input("enter CGPA: ")
        state = input("enter state: ")
        student[reg] = {"name": name, "course": course, "cgpa": cgpa, "state": state}
        print("Student added successfully!")


def search_student():
    print("Search Student ")
    reg = input("enter registration number: ")
    if reg in student:
        print("Record Found:")
        print("Reg No :", reg)
        print("Name :", student[reg]["name"])
        print("Course :", student[reg]["course"])
        print("CGPA :", student[reg]["cgpa"])
        print("state :", student[reg]["state"])
    else:
        print("Student not found!")


def update_student():
    print("Update Student ")
    reg = input("Enter Registration number: ")
    if reg in student:
        print("Leave blank to keep old value.")
        name = input(f"name ({student[reg]['name']}): ") or student[reg]["name"]
        course = input(f"Course ({student[reg]['course']}): ") or student[reg]['course']
        cgpa = input(f"CGPA ({student[reg]['cgpa']}): ") or student[reg]['cgpa']
        state = input(f"State ({student[reg]['state']}): ") or student[reg]['state']
        student[reg] = {"name": name, "course": course, "cgpa": cgpa, "state": state}
        print("record updated successfully!")
    else:
        print("student not found!")


def delete_student():
    print("Delete Student ")
    reg = input("enter registration number: ")

    if reg in student:
        del student[reg]
        print("student deleted successfully!")

    else:
        print("student not found !")


def display_all():
    print(" All Students ")
    for reg, info in student.items():
        print("Reg No :", reg)
        print("Name   :", info["name"])
        print("Course :", info["course"])
        print("CGPA   :", info["cgpa"])
        print("State  :", info["state"])


while True:
    print(" STUDENT RECORD SYSTEM ")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    ch = int(input("enter your choice: "))

    if ch == 1:
        add_student()
    elif ch == 2:
        search_student()
    elif ch == 3:
        update_student()
    elif ch == 4:
        delete_student()
    elif ch == 5:
        display_all()
    elif ch == 6:
        print("Exiting")
        break
    else:
        print("invalid choice ! Try again")
