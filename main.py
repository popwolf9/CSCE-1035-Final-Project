from student import Student
from faculty import Faculty
from course import Course
from utils import load_students, save_students

faculty_list = {
    "Gooran": Faculty("F01", "Hadiseh Gooran", "CS"),
    "Swain": Faculty("F02", "Justin Swain", "Math")
}

course_list = {
    "CSCE1010": Course("CSCE1010", "Intro to CS"),
    "MATH1710": Course("MATH1710", "Calculus I")
}

students = load_students()

def display_menu():
    print("\nUniversity of North Texas")
    print("1. Create Student")
    print("2. Enroll Student in Course")
    print("3. Assign Faculty to Course")
    print("4. List All Students")
    print("5. List Courses and Faculty")
    print("6. List Enrolled Students in a Course")
    print("0. Exit")

while True:
    display_menu()
    choice = input("Select an option: ")

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Name: ")
        major = input("Major: ")
        students[sid] = Student(sid, name, major)
        save_students(students)
        print("Student added.\n")

    elif choice == "2":
        sid = input("Student ID: ")
        cid = input("Course ID: ")
        if sid in students and cid in course_list:
            students[sid].enroll(cid)
            course_list[cid].enroll_student(sid)
            save_students(students)
            print("Student enrolled.")
        else:
            print("Invalid student or course ID.")

    elif choice == "3":
        fid = input("Faculty ID: ")
        cid = input("Course ID: ")
        if fid in faculty_list and cid in course_list:
            faculty_list[fid].assign_course(cid)
            course_list[cid].assign_instructor(fid)
            print("Faculty assigned.")
        else:
            print("Invalid faculty or course ID.")

    elif choice == "4":
        for s in students.values():
            print(f"{s.student_id} - {s.name} ({s.major}) - Courses: {', '.join(s.enrolled_courses)}")

    elif choice == "5":
        for cid, course in course_list.items():
            instructor = course.instructor or "None"
            print(f"{cid}: {course.name} - Instructor: {instructor}")

    elif choice == "6":
        cid = input("Course ID: ")
        if cid in course_list:
            print(f"Students in {cid}: {', '.join(course_list[cid].students)}")
        else:
            print("Invalid course ID.")

    elif choice == "0":
        break

    else:
        print("Invalid option. Try again.")

