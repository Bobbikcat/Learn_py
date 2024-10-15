def read_file(file):
    with open(file, 'a+', encoding='utf-8') as f:
        f.seek(0)
        data = f.read()
        print(f'\n{data}\n')


def read_lines(file):
    with open(file, 'a+', encoding='utf-8') as lines:
        lines.seek(0)
        for line in lines:
             print(line.strip())


def write_file(text_new, file):
        with open(file, 'a', encoding='utf-8') as content:
            content.write('\n\n')
            content.write(text_new)


def copy_binary(file_copy):
        with open(file_copy, 'rb') as copy:
            data = copy.read()
        with open('data.bin', 'wb') as binary:
            binary.write(data)



if __name__ == '__main__':
    text_file = 'data.txt'
    read_file(text_file)

    input('\nNext step - press [Enter]')
    user_input = input('\nWrite something to add this\n>>>')

    write_file(text_new=user_input, file=text_file)
    read_file(text_file)
    input('\nNext step - press [Enter]\n')

    read_lines(text_file)
    input('\nNext step - press [Enter]\n')

    copy_binary(text_file)
