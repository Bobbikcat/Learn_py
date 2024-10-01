# Text Analyser

p_marks = list('''!@#$%^&*()_+-=`~{}[];:/|\\?.,<>'"''')
vowels = list('aeiouy')
vowels_count = 0
new_string = ''
long_word = ''
words_list = []


def input_handler():
    global new_string
    global words_list
    for el in user_input:
        for mark in p_marks:
            if mark == el:
                break
        else:
            new_string += el
    else:
        words_list = new_string.upper().split()
        print(f'Number of words: {len(words_list)}')


def vowels_counter():
    global vowels_count
    for letter in new_string.lower():
        for v in vowels:
            if v == letter:
                vowels_count += 1
                break
    print(f'Numbers of vowels: {vowels_count}')


def longest_word():
    global long_word
    long_word = max(words_list, key=len)
    print(f'The longest word: {long_word}')


def words_doubles():
    repeated_words_amt = 0
    repeated_words_list = [['none']]
    temp_list = []
    match = 0

    for word in words_list:
        for current in words_list:
            if current == word:
                repeated_words_amt += 1
        else:
            temp_list = [word, repeated_words_amt]
            for value in repeated_words_list:
                if value == temp_list:
                    match += 1
            else:
                if match < 1:
                    repeated_words_list.append(temp_list)
                repeated_words_amt = 0
                match = 0
    else:
        print('\nWord Statistic:\n')
        _bool = False
        for element in repeated_words_list:
            if _bool:
                if element[1] > 1:
                    print(f'" {element[0]} ": {element[1]} words')
                else:
                    print(f'" {element[0]} ": {element[1]} word')
            else:
                _bool = True
                continue


# 'Run program'
user_input = input('Type something for Analyse: ')
hash_input = hash(user_input)
print('\nANALYSING..')
print(f'operation id: {hash_input}\n')

input_handler()
vowels_counter()
longest_word()
words_doubles()
