#  A Service class for Repository


class Service:
    def __init__(self, repository, cls_validator):
        self.repository = repository
        self.cls_validator = cls_validator

    def view_library(self):
        return self.repository.view_library()

    def add_book(self, new_book):
        self.cls_validator.f_validate(new_book)
        self.check_book(new_book.title)
        self.repository.add_book(new_book)

    def check_book(self, new_title):
        if new_title in self.repository.view_library():
            raise NameError('\nThis book in the Library already exist !\n')

    def update_book(self, old_title, new_book):
        return self.repository.update_book(old_title, new_book)

    def remove_book(self, del_book):
        return self.repository.remove_book(del_book)

    def find_book(self, book):
        if book in self.repository.view_library():
            return list(self.repository.view_library()[book].values())
        raise NameError('\nCan\'t find this book now...\nreturn to user menu..\n')

    def change_status(self, book_name, status):
        if status:
            print('\nIN-STOCK: YES')
            available = input('Mark this book <Unavailable> ? enter " Y/N ": ')
            if available.upper().strip() == 'Y':
                self.repository.change_status(book_name, False)
                print('\n*Now your book NOT-in-Stock*')
            else:
                print('\n*return to menu*')
        elif status is False:
            print('\nIN-STOCK: NO')
            available = input('Mark this book <Available> ? enter " Y/N ": ')
            if available.upper().strip() == 'Y':
                self.repository.change_status(book_name, True)
                print('\n*Now your book IN-Stock*')
            else:
                print('\n*return to menu*')
        else:
            available = input(
                '''\n> Book in the Library, but status not defined <\nTo set your status, enter:\n"A" - Available | "U" - Unavailable | *press any key to leave*: ''')
            if available.upper().strip() == 'A':
                self.repository.change_status(book_name, True)
                print('\n*Now your book IN-Stock*')
            elif available.upper().strip() == 'U':
                self.repository.change_status(book_name, False)
                print('\n*Now your book NOT-in-Stock*')
            else:
                print('\n*return to menu*')
