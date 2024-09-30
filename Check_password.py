# Check Password
user_password = input('Create your password: ')
print(f'Success! Your password: {user_password}\n')

check_password = input('Enter your password: ')
while user_password != check_password:
    print('\nInvalid password. Access denied.')
    check_password = input('Enter your password: ')
else:
    print('\nSuccess. Login completed.')
