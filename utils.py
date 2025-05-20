import csv
from student import Student

CSV_FILE = "students.csv"

def load_students():
    students = {}
    try:
        with open(CSV_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                student = Student.from_dict(row)
                students[student.student_id] = student
    except FileNotFoundError:
        pass
    return students

def save_students(students):
    with open(CSV_FILE, "w", newline="") as f:
        fieldnames = ["ID", "Name", "Major", "Courses"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for student in students.values():
            writer.writerow(student.to_dict())

