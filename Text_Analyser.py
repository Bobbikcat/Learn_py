# Text Analyser
cleared_string = ''
words_list = []


def input_handler(str_input):
    global cleared_string
    global words_list

    for el in str_input:
        if el.isalpha() or el == ' ':
            cleared_string += el
    else:
        words_list = cleared_string.upper().split()
        print(f'Number of words: {len(words_list)}')


def vowels_counter():
    vowels = 'aeiouyаеёиоуыэюя'
    vowels_count = 0

    for v in vowels:
        vowels_count += cleared_string.count(v)
    else:
        print(f'Numbers of vowels: {vowels_count}')


def longest_word():
    if words_list:
        long_word = max(words_list, key=len)
        print(f'The longest word: {long_word}')


def words_doubles():
    if words_list:
        repeated_words_amt = 0
        unique_words = set(words_list)

        print('\nWord Statistic:\n')
        for word in unique_words:
            repeated_words_amt += words_list.count(word)
            temp_list = [word, repeated_words_amt]
            repeated_words_amt = 0

            if temp_list[1] > 1:
                print(f'" {temp_list[0]} ": {temp_list[1]} words')
            else:
                print(f'" {temp_list[0]} ": {temp_list[1]} word')


# 'Run program'
while True:
    user_input = input('Type something for Analyse: ')
    if user_input:
        hash_input = hash(user_input)
        print('\nANALYSING..')
        print(f'operation id: {hash_input}\n')

        input_handler(user_input)
        vowels_counter()
        longest_word()
        words_doubles()
        break
    else:
        print('Error: No input taken! Try again\n')
        continue
