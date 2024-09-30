# Elections

def check_input(arg_input):
    if arg_input != 'Y' and arg_input != 'N':
        print('\nError: Invalid input. Try again..')
        exit()


def passing_score(_age, _country, _record):
    age_issue = 'You are under 18'
    country_issue = 'You are not a citizen'
    record_issue = 'You have a criminal record'
    issue_list = []

    if _age == 'N':
        issue_list.append(age_issue)
    if _country == 'N':
        issue_list.append(country_issue)
    if _record == 'Y':
        issue_list.append(record_issue)

    if len(issue_list) <= 0:
        print('\nVerification passed! You CAN vote!')
    else:
        print('\nVerification failed.. You CAN NOT vote.\nReasons:')
        for reason in issue_list:
            print(f'{reason}')


print('(type: "Y" for YES, "N" for NO)\n')

age = input('Are you 18 or older? -> ')
age = age.upper()
check_input(age)

country = input('Are you a citizen of Russia? -> ')
country = country.upper()
check_input(country)

record = input('Do you have a criminal record? -> ')
record = record.upper()
check_input(record)

passing_score(age, country, record)