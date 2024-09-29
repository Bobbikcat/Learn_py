# Countdown
try:
    user_num = float(input('Enter a positive Integer: '))
except ValueError:
    print('Error: Not a number.')
else:
    user_num = int(abs(user_num))
    print('Countdown\n')
    while user_num > -1:
        print(user_num)
        user_num -= 1
finally:
    print('\nСompleted..')