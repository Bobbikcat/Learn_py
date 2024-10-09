import cowsay as _c_
from To_do_list import ToDoList as tdl

greet = _c_.get_output_string('kitty', 'WELCOME TO TASKER')


def add_form():
    user_input = input('\nEnter New Task: ')
    todo.add_task(user_input)


def remove_form():
    try:
        todo.list_tasks()
        user_input = input('\n< Deleting task >\nEnter number of task: ')
        todo.remove_task(user_input)
    except Exception as e:
        print(e)


def mark_form():
    try:
        todo.list_tasks()
        user_input = input('\n< Marking task >\nEnter number of task: ')
        todo.complete_task(user_input)
    except Exception as e:
        print(e)


def run():
    while True:
        print('_' * 20, '\n[ Main Menu ]\n')
        print(
            '1. List Tasks\n'
            '2. Add Task\n'
            '3. Remove Task\n'
            '4. Mark Task\n'
            '5. Exit\n'
        )
        user_input = input('Enter number of action: ')
        print('_' * 20)
        if user_input.strip() == '1':
            try:
                todo.list_tasks()
            except Exception as e:
                print(e)
        elif user_input.strip() == '2':
            add_form()
        elif user_input.strip() == '3':
            remove_form()
        elif user_input.strip() == '4':
            mark_form()
        elif user_input.strip() == '5':
            exit()
        else:
            print('\nInvalid input..')


if __name__ == '__main__':
    # print('\nWELCOME TO TASKER')
    print(greet)
    print('_' * 60)
    todo = tdl()
    run()
