from typing import List


class Student:
    # default parameters are defined when the class is created.
    # This is just creating names to the same list.
    # a fix: grades: Optional[List[int]] = None    self.grades = grades or []
    def __init__(self, name: str, grades: List[int] = []):  # This is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("bob")
rolf = Student("rolf")
bob.take_exam(90)
print(bob.grades)
# rolf will also have 90
print(rolf.grades)
