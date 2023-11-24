def sorter(name_list):
    name_list.sort()
    for i in range(len(name_list)):
        print(f"{i + 1}. {name_list[i].strip()}")

def fileRead():
    global students
    with open("students.txt", "r") as file:
        students = [line.strip() for line in file.readlines()]
    return students

def fileWrite():
    global students
    with open("students.txt", "w") as file:
        for student in students:
            file.write(student + '\n')

def main():
    global students
    students = fileRead()
    sorter(students)
    fileWrite()

main()