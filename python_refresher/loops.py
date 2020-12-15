var = 'hello, world'

for c in var: # iterable are strings, lists, sets, tuples, etc
    print(c)

my_list = [1, 3, 5, 7, 9]

for n in my_list:
    print(n ** 2)

user_wants_number = True

while user_wants_number:
    print(10)
    user_input = input('Should we print again? (y/n) ')
    if user_input == 'n':
        user_wants_number = False
    
