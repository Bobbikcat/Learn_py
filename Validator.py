#  Validator class for Service
class Validator:
    def __init__(self):
        pass

    def f_validate(self, new_book):
        if new_book.title == '':
            raise ValueError('\nERROR: \'TITLE\' can not be empty !\nreturn to user menu..\n')
        if new_book.author == '':
            raise ValueError('\nERROR: \'AUTHOR\' can not be empty !\nreturn to user menu..\n')
        if new_book.year == '':
            raise ValueError('\nERROR: \'YEAR\' can not be empty !\nreturn to user menu..\n')
