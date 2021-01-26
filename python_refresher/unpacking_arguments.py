def multiple(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg

    return total

print(multiple(1, 3, 5))
print(multiple(-1))

def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return 'No valid operator provided to apply().'

print(apply(1, 3, 6, 7, operator='+'))
print(apply(1, 3, 6, 7, operator='*'))



def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))
print(add(x=3, y=5))

nums = {'x': 15, 'y': 25}
#print(add(x=nums['x'], y=nums['y']))
print(add(**nums))
