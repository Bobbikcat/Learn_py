# Library. 1 - Create.

# "only for test below"
# begin
test_lib = {}
# end

# Program
library_dict = {
    'The Great Gatsby': {
        'Author': 'F. Scott Fitzgerald',
        'Year': '1925',
        'In-stock': 'No'
    },
    'Nineteen Eighty Four': {
        'Author': 'George Orwell',
        'Year': '1949',
        'In-stock': 'Yes'
    },
    'Crime and Punishment': {
        'Author': 'Fyodor Dostoevsky',
        'Year': '1866',
        'In-stock': 'Yes'
    },
    'The Master and Margarita': {
        'Author': 'Mikhail Bulgakov',
        'Year': '1967',
        'In-stock': 'No'
    }
}


def user_menu():
    print('1. View Library')
    user_input = input('Select an action and enter its number: ')
    if user_input.strip() == '1':
        book_list_view(library_dict)
        # book_list_view(test_lib)
    else:
        print('\nInvalid input.. Try again..\n')
        user_menu()


def book_list_view(library):
    # print(library.keys()) #Но так не красивый вывод.
    books_list = []
    book_index = 0

    if library:
        print('\nLIBRARY BOOKS:\n')
        for name in library:
            books_list.append(name)
            print(books_list[book_index])
            book_index += 1
        else:
            print('_' * 20)
    else:
        print('\n- The library of books is empty -\n' + '_' * 20)


# Run program
print('WELCOME TO LIBRARY !\n')
user_menu()
