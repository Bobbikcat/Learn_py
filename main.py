# Sum of Even Numbers. (обернул, но зачем ?)
def even_sum():
    _even = 0
    for i in range(1, 100):
        if i % 2 == 0:
            _even += i
    return _even


result = even_sum()
print(result)

# Squares of odd numbers
odd_list = [n ** 2 for n in range(1, 10) if n % 2 != 0]
print(odd_list)

# Negative numbers counter
nums_amt = 0

while True:
    try:
        _bool = True
        user_input = float(input('\nEnter a negative number: '))
    except ValueError:
        print('ERROR: Invalid input. Try again..\n')
        _bool = False
    finally:
        if _bool:
            if user_input == abs(user_input):
                nums_amt += 1
                print(f'ENTERED: {user_input}')
                print('Not a negative number! Try again..')
            else:
                print(f'ENTERED: {user_input}')
                print(f'Entered numbers: {nums_amt + 1}')
                break
