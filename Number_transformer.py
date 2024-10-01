# Number Transformer
words_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

try:
    int_to_text = float(input('Enter a number from 1 to 5: '))

except ValueError:
    print('\nError: Not a number.')
else:
    int_to_text = int(int_to_text)
    if 1 <= int_to_text <= 5:
        for i in words_dict:
            if i == int_to_text:
                print('\nYou entered number: ', words_dict[i])
                break
    else:
        print('\nYour number not in range.')
finally:
    print('\nЗавершение работы...')