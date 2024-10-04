# Addition of list elements
num_list1 = []
num_list2 = []
sum_list = []


def equalizer(l1, l2):
    global num_list1, num_list2
    num_list1 = l1.split()
    num_list2 = l2.split()

    if len(num_list1) != len(num_list2):
        x = abs(len(num_list1) - len(num_list2))
        for each in range(x):
            if len(num_list1) > len(num_list2):
                num_list2.append('0')
            elif len(num_list1) < len(num_list2):
                num_list1.append('0')
            else:
                break


def sum_values():
    global num_list1, num_list2, sum_list
    list_length = len(num_list1)

    for value in range(0, list_length):
        try:
            num_type = float(num_list1[value]) + float(num_list2[value])
            if num_type % 1 == 0:
                sum_list.append(int(num_type))
            else:
                sum_list.append(num_type)
        except ValueError:
            print('ERROR: An invalid value was entered..')
            exit()
    else:
        print(f'\nSums of corresponding values:\n{sum_list}')


input_1 = input('List 1. Enter any numbers separated by spaces: ')
input_2 = input('List 2. Enter any numbers separated by spaces: ')
equalizer(input_1, input_2)
sum_values()
