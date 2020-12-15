grades = [77, 80, 90, 95, 100]
tuple_grades = (77, 80, 90) # immutable and ordered
set_grades = {77, 80, 90} # unique and unordered

print(sum(grades) / len(grades))

print(set_grades)

###

# list operations
grades.append(20)
grades[0] = 66
print(grades)
print(grades[0])

# tuple operations
tuple_grades = tuple_grades + (100,) # or ... + 100,
print(tuple_grades)

# set operations
set_grades.add(43)
set_grades.add(43)
print(set_grades)

your_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}
# 1, 3, 5
print(your_numbers.intersection(winning_numbers))
# 1, 2, 3, 4, 5, 7, 9, 11
print(your_numbers.union(winning_numbers))
# 3, 4
print({1,2,3,4}.difference({1,2}))
