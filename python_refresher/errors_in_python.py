def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


grades = [78, 99, 85, 100]
grades = []

print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}.")
except ZeroDivisionError as e:
    print(e)
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you")


students = [
    {"name": "Bob",  "grades": [75, 90]},
    {"name": "Rolf", "grades": [50]},
    {"name": "Jen",  "grades": [100, 90]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")
