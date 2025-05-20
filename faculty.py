class Faculty:
    def __init__(self, faculty_id, name, department):
        self.faculty_id = faculty_id
        self.name = name
        self.department = department
        self.courses = []

    def assign_course(self, course_id):
        if course_id not in self.courses:
            self.courses.append(course_id)

