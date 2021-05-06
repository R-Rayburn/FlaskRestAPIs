class Student:
    def __init__(self, name):
        self.name = name
        self.grades = (89, 90, 93, 78, 90)

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Rolf")
print(student.name + " has an average of " + str(student.average()))
