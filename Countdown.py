# Countdown
try:
    user_num = int(input('Enter a positive Integer: '))
except ValueError:
    print('Error: Invalid Value.')
else:
    if user_num >= 0:
        print('Countdown\n')
        while user_num > -1:
            print(user_num)
            user_num -= 1
    else:
        print('Error: Your number not a positive!')
finally:
    print('\nСompleted..')
