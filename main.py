print('(type: "Y" for YES, "N" for NO)\n')

age = input('Are you 18 or older? -> ')
if age == 'Y' or age == 'y':
    country = input('Are you a citizen of Russia? -> ')
    if country == 'Y' or country == 'y':
        additional = input('Do you have a criminal record? -> ')
        if additional == 'N' or additional == 'n':
            print('\nПроверка пройдена: Вы можете проголосовать на выборах.')
        elif additional == 'Y' or additional == 'y':
            print('\nВам не разрешено голосовать.')
        else:
            print('\nОшибка ввода.. Начните заного.')
    elif country == 'N' or country == 'n':
        print('\nВам не разрешено голосовать.')
    else:
        print('\nОшибка ввода.. Начните заного.')
elif age == 'N' or age == 'n':
    print('\nВам не разрешено голосовать.')
else:
    print('\nОшибка ввода.. Начните заного.')
    