known_people = ['john', 'anna', 'mary']

person = input('Enter the person you know: ')
if person in known_people:
    print('you know {}!'.format(person))
else:
    print('you don\'t know {}'.format(person))


## Exercise

def who_do_you_know():
    return input('Who do you know? ("," sep) ').replace(' ', '').split(',')

def ask_user(known_people):
    name = input('Give me a name: ')
    if name in known_people:
        print('you know {}'.format(name))
    else:
        print('you don\'t know {}'.format(name))

know = who_do_you_know()
ask_user(know)
