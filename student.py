import csv

class Student:
    def __init__(self, student_id, name, major, enrolled_courses=None):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.enrolled_courses = []

    def enroll(self, course_id):
        if course_id not in self.enrolled_courses:
            self.enrolled_courses.append(course_id)

    def to_dict(self):
        return {
            "ID": self.student_id,
            "Name": self.name,
            "Major": self.major,
            "Courses": ";".join(self.enrolled_courses)
        }

    def from_dict(data):
        return Student(
            data["ID"],
            data["Name"],
            data["Major"],
            data["Courses"].split(";") if data["Courses"] else []
        )

