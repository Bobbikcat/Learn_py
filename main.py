# Elections
user_input = ['y', 'Y', 'n', 'N']


def check_input(arg_input):
    user_pass = False
    for i in user_input:
        if i == arg_input:
            user_pass = True
            break
    if not user_pass:
        print('\nError: Invalid input. Try again..')
        exit()


def passing_score(_age, _country, _record):
    age_issue = 'You are under 18'
    country_issue = 'You are not a citizen'
    record_issue = 'You have a criminal record'
    issue_list = []

    if _age == 'n' or _age == 'N':
        issue_list.append(age_issue)
    if _country == 'n' or _country == 'N':
        issue_list.append(country_issue)
    if _record == 'y' or _record == 'Y':
        issue_list.append(record_issue)

    if len(issue_list) <= 0:
        print('\nVerification passed! You CAN vote!')
    else:
        print('\nVerification failed.. You CAN NOT vote.\nReasons:')
        for reason in issue_list:
            print(f'{reason}')


print('(type: "Y" for YES, "N" for NO)\n')

age = input('Are you 18 or older? -> ')
check_input(age)

country = input('Are you a citizen of Russia? -> ')
check_input(country)

record = input('Do you have a criminal record? -> ')
check_input(record)

passing_score(age, country, record)
