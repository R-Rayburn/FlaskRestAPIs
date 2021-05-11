from typing import List


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


print(list_avg(123))


class Book:
    def __init__(self):
        pass

    # Use string version of class when returning
    # the class you are in.
    @classmethod
    def hardconver(cls) -> "Book":
        return cls()
