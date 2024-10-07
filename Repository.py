#  Repository class for Library

class Repository:
    def __init__(self):
        # self.library_dict = {}  #--only for test empty dict--
        self.library_dict = {
            'The Great Gatsby': {
                'Author': 'F. Scott Fitzgerald',
                'Year': '1925',
                'In-stock': False
            },
            'Nineteen Eighty Four': {
                'Author': 'George Orwell',
                'Year': '1949',
                'In-stock': True
            },
            'Crime and Punishment': {
                'Author': 'Fyodor Dostoevsky',
                'Year': '1866',
                'In-stock': True
            },
            'The Master and Margarita': {
                'Author': 'Mikhail Bulgakov',
                'Year': '1967',
                'In-stock': False
            }
        }

    def view_library(self):
        return self.library_dict

    def add_book(self, new_book):
        self.library_dict[new_book.title] = {f'Author': f'{new_book.author}', f'Year': f'{new_book.year}',
                                             f'In-stock': None}
        # print(self.library_dict)

    def update_book(self, old_title, new_book):
        x = self.remove_book(old_title)
        self.add_book(new_book)
        return x

    def remove_book(self, del_book):
        if del_book in self.library_dict:
            self.library_dict.pop(del_book)
            return del_book
        raise Exception('\nCan\'t find this book now...\nreturn to user menu..\n')

    def change_status(self, book, status):
        self.library_dict[book]['In-stock'] = status
