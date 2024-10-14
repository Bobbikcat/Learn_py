def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        data_r = f.read()
        print(f'\n{data_r}\n')


def write_file(adding, to_file):
    with open(adding, 'r', encoding='utf-8') as f_new:
        lines = f_new.readlines()
    with open(to_file, 'a', encoding='utf-8') as f_target:
        f_target.write('\n\n')
        for el in lines:
            f_target.write(f'{el}')


def read_lines(file):
    with open(file, 'r', encoding='utf-8') as f_lines:
        for line in f_lines:
            print(line.strip())


def copy_binary(to_copy):
    with open(to_copy, 'rb') as copy:
        b_data = copy.read()
    with open('data_binary.txt', 'wb') as b_file:
        b_file.write(b_data)


if __name__ == '__main__':
    main_file = 'data.txt'
    read_file(main_file)
    input('\nNext step: ')

    new_file = 'data_1.txt'
    write_file(adding=new_file, to_file=main_file)
    read_file(main_file)
    input('\nNext step: ')

    read_lines(main_file)
    input('\nNext step: ')

    copy_binary(main_file)
