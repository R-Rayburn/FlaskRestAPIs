add = lambda x, y: x + y

print(add(5, 7))
print((lambda x, y: x + y)(5, 7))


def double(x):
    return x * 2

seq = [1, 3, 5, 9]

# doubled = [double(x) for x in seq]
doubled = list(map(lambda x: x * 2, sequence))
