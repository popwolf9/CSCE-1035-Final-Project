class Course:
    def __init__(self, course_id, name, instructor=None):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
        self.students = []

    def assign_instructor(self, faculty_id):
        self.instructor = faculty_id

    def enroll_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)

