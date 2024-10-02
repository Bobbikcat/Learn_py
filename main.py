# Sum of Even Numbers
even_sum = 0

for i in range(1, 100):
    if i % 2 == 0:
        even_sum += i
print(even_sum)

# Squares of odd numbers
odd_list = [n ** 2 for n in range(1, 10) if n % 2 != 0]
print(odd_list)

# Negative numbers counter
nums_amt = 0


def cycle_attempt():
    global nums_amt
    pass_bool = True
    try:
        user_input = float(input('\nEnter a negative number: '))
    except ValueError:
        print('Error: Invalid input.')
        pass_bool = False
    finally:
        if pass_bool:
            if user_input == abs(user_input):
                nums_amt += 1
                print('ENTERED: ' + str(user_input))
                print('Not a negative number! Try again..')
                cycle_attempt()
            else:
                print('ENTERED: ' + str(user_input))
                print('Attempts: ' + str(nums_amt + 1))


cycle_attempt()