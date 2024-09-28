#
# def say_hello():
#     print('Hello, Python!\n')
#
# def repeat_msg(message):
#     print(f'{message}\n' * 3)
#
# say_hello()
# repeat_msg('Hi')


# def f_multiply(num1, num2):
#     return num1 * num2
#
# print(f_multiply(2, 2))


# new_text = 'string'
# new_list = ['A', 1, 'B']
#
# def var_info(arg1):
#     var_type = type(arg1)
#     var_length = len(arg1)
#     print(f'Type: {var_type}\nLength: {var_length}\n')
#
# var_info(new_text)
# var_info(new_list)


# Key words 1
def max_of_two(x, y):
    return max(x, y)


print(max_of_two(2, 4))
print('_' * 10)


# Key words 2
def f_empty():
    pass


# Key words 3
def even_numbers(n):
    for value in range(0, n + 1):
        if value % 2 == 0:
            yield value


r = 10
for i in even_numbers(r):
    print(i)
print('_' * 10)


# Key words 4
def test_max():
    assert max_of_two(2, 4) == 4, 'Error. Max number is 4\n'
    assert max_of_two(5, 2) == 5, 'Error. Max number is 5\n'
    assert max_of_two(1, -3) == 1, 'Error. Max number is 1\n'
    assert max_of_two(0, 0) == 0, 'Error. Max number is 1\n'


test_max()
print('No Errors.')
