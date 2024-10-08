#  A Console class for Service

from HW_Library.Library import Library


class Console:
    def __init__(self, service):
        self.service = service

    def book_list_view(self):
        all_books = self.service.view_library()

        if all_books:
            print('\nLIBRARY BOOKS:\n')
            for index, (k, v) in enumerate(all_books.items(), start=1):
                print(f'[{index}] {k}')
        else:
            print('\n- The library of books is empty -\nreturn to user menu..\n')

    def update_book(self, title, book):
        user_choice = input('Would you like to UPDATE this book ?\n1. YES\n2. NO (press any key)\n>>> ')
        if user_choice.strip() == '1':
            x = self.service.update_book(title, book)
            print(f'\nYOUR BOOK "{x}" WAS UPDATED !\n')

    def add_book(self):
        new_title = input('\nEnter a new book - TITLE: ')
        new_author = input('\nEnter a new book - AUTHOR: ')
        new_year = input('\nEnter a new book - YEAR: ')
        new_book = Library(new_title, new_author, new_year)
        try:
            self.service.add_book(new_book)
            print('\nNEW BOOK ADDED !\n')
        except ValueError as empty:
            print(empty)
        except NameError as exist:
            print(exist)
            self.update_book(new_title, new_book)

    def remove_book(self):
        delete_book = input('\nEnter a NAME of the book: ').strip()
        try:
            x = self.service.remove_book(delete_book)
            print(f'\nYOUR BOOK "{x}" WAS REMOVED..!\n')
        except Exception as e:
            print(e)

    def find_book(self):
        book_name = input('\nEnter a NAME of the book: ').strip()
        try:
            d = self.service.find_book(book_name)
            print(f'\nThe book - " {book_name} "\nAuthor: {d[0]}\nReleased in {d[1]}')
            self.service.change_status(book_name, d[2])
        except NameError as nothing:
            print(nothing)

    # Menu for user input
    def run(self):
        while True:
            print('_' * 20, "\nWELCOME TO LIBRARY !")
            print('\n1. View Library')
            print('2. Add a New Book')
            print('3. Delete a Book')
            print('4. Find a Book')
            print('5. Exit')
            user_input = input('\nSelect an action and enter its number: ')
            if user_input.strip() == '1':
                self.book_list_view()
            if user_input.strip() == '2':
                self.add_book()
            if user_input.strip() == '3':
                self.remove_book()
            if user_input.strip() == '4':
                self.find_book()
            if user_input.strip() == '5':
                exit()
