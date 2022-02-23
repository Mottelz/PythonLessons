from student import Student


def find_student_by_id(students, target_id):
    for s in students:
        if s.id == target_id:
            return s


def main():
    student_list = [
        Student("Mottel", "Zirkind", 12),
        Student("Bentzy", "Zirkind", 13)
    ]
    print(find_student_by_id(student_list, 13))


if __name__ == "__main__":
    main()
