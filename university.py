class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)

    def show_courses(self):
        if not self.courses:
            print(f"{self.name} is not enrolled in any courses.")
        else:
            print(f"{self.name}'s enrolled courses:")
            for course in self.courses:
                print(f" - {course}")


class Classroom:
    def __init__(self, room_name, capacity):
        self.room_name = room_name
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True
        return False

    def roster(self):
        if not self.students:
            print(f"No students in classroom {self.room_name}.")
        else:
            print(f"Students in classroom {self.room_name}:")
            for student in self.students:
                print(f" - {student.name}")


if __name__ == "__main__":

    alice = Student("Alice", "S001")
    bob = Student("Bob", "S002")
    charlie = Student("Charlie", "S003")

    classroom = Classroom("Room 101", 2)

    for student in [alice, bob, charlie]:
        if classroom.add_student(student):
            print(f"{student.name} added to {classroom.room_name}.")
        else:
            print(f"{student.name} could not be added; classroom is full.")

    print()
    classroom.roster()

    print()
    alice.enroll("Math")
    alice.enroll("Physics")
    alice.show_courses()
    bob.show_courses()