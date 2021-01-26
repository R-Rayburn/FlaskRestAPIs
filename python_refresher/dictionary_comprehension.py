users = [
    (0, 'bob', 'password'),
    (1, 'rolf', 'bob123'),
    (2, 'jose', 'longp4assword'),
    (3, 'username', '1234')
]

username_mapping = {user[1]: user for user in users}

#print(username_mapping['bob'])

username_input = input('enter username: ')
password_input = input('enter password: ')

_, username, passowrd = username_mapping[username_input]

if password_input == password:
    print('loggedin')
else:
    print('incorrect')
