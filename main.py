students = []
filename = "student.txt"


def get_name():
    student_name = []
    for student in students:
        student_name.append(student["name"].title())
    return student_name


def show_name():
    name = get_name()
    print(name)


def add_name(name):
    student = {"name": name}
    students.append(student)


def save_file(student):
    try:
        f = open(filename, "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open(filename, "r")
        for student in f.readlines():
            add_name(student)
        f.close()
    except Exception:
        print("Could not read file")


read_file()
show_name()

student_name = input("Enter student name: ")
save_file(student_name)
add_name(student_name)
