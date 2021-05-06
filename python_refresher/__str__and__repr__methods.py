class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Prints by default
    def __str__(self):
        return f"Name: {self.name} | Age: {self.age}"
    # Unabiguous string to be able to re-create object
    # used in python debugger
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

bob = Person("Bob", 35)
print(bob)
print(bob.__repr__())
