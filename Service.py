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
            return list(self.repository.view_library()[book].values())  # да, это гениально, спасибо :3
        raise NameError('\nCan\'t find this book now...\nreturn to user menu..\n')

    def change_status(self, book, status):
        self.repository.change_status(book, status)
