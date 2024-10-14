def read_file(file):
    if checker(file):
        with open(file, 'r', encoding='utf-8') as reading:
            data_read = reading.read()
            print(f'\n{data_read}\n')


def write_file(adding, to_file):
    if checker(adding) and checker(to_file):
        with open(adding, 'r', encoding='utf-8') as file_new:
            lines = file_new.readlines()
        with open(to_file, 'a', encoding='utf-8') as file_target:
            file_target.write('\n\n')
            for el in lines:
                file_target.write(f'{el}')


def read_lines(file):
    if checker(file):
        with open(file, 'r', encoding='utf-8') as file_lines:
            for line in file_lines:
                print(line.strip())


def copy_binary(to_copy):
   if checker(to_copy):
        with open(to_copy, 'rb') as copy:
            binary_data = copy.read()
        with open('data_binary.txt', 'wb') as binary_file:
            binary_file.write(binary_data)

def checker(text_file):
    try:
        test = open(text_file, 'r', encoding='utf-8')
        test.close()
        return True
    except OSError: # Он ведь Parent для файловых исключений или нет ?
        print(f'Error: File "{text_file}" error..')
        exit('End program')
        # Не понимаю, почему тут eсли переменная bool,
        # то он выдает OSError системным красным цветом.
        # Eсли переменной нет, выдает Name Error.
        # Отлов этими разными эксэптами не помогает, и
        # так же не помогает ни Exeption, ни BaseExeption...
        # как ни крути - не ловит, и выдает красным цветом ошибки.

if __name__ == '__main__':
    main_file = 'data.txt'
    new_file = 'data_1.txt'

    read_file(main_file)
    input('\nNext step: ')

    write_file(adding=new_file, to_file=main_file)
    read_file(main_file)
    input('\nNext step: ')

    read_lines(main_file)
    input('\nNext step: ')

    copy_binary(main_file)
