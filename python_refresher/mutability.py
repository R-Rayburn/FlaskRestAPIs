a = 8597
b = 8597

print(a)
print(b)

print(id(a))
print(id(b))

# gives 8598 the name of a
a = 8598

print(id(a))
print(id(b))


a = "hello"
b = a

print(id(a))
print(id(b))

a += "world"

print(a)
print(b)
