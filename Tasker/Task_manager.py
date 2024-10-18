class TaskManager:
    c_BLACK = '\033[30m'
    c_RED = '\033[31m'
    c_GREEN = '\033[32m'
    c_YELLOW = '\033[33m'
    c_BLUE = '\033[36m'
    bg_BLACK = '\033[40m'
    bg_WHITE = '\033[47m'
    s_END = '\033[0m'
    s_FADED = '\033[2m'
    s_ITALIC = '\033[3m'

    def __init__(self, service):
        self.service = service

    @staticmethod
    def __exception_print(exception):
        print(f'{TaskManager.c_RED}Error: {exception}{TaskManager.s_END}')

    def view_tasks(self):
        try:
            print(f'\n{self.bg_BLACK}*** TASKER ***{self.s_END}\n')
            self.service.view_tasks()
            print(f'\n* {self.c_GREEN}{self.s_ITALIC}Completed{self.s_END} '
                  f'| {self.c_RED}{self.s_ITALIC}Not Completed{self.s_END} *'
                  )
        except Exception as e:
            self.__exception_print(e)
            return e

    def add_task(self):
        try:
            user_input = input('Type your Task: ')
            self.service.add_task(description=user_input)
            print(f'\nYour Task has been {self.c_BLUE}Added !{self.s_END}')
        except Exception as e:
            self.__exception_print(e)

    def remove_or_complete(self, mode=''):
        try:
            _error = self.view_tasks()
            if not _error:
                _help, _prefix, mode = self.service.get_mode(mode=mode)
                user_input = int(input(f'\nEnter number of task to {mode}: '))
                respond = self.service.remove_or_complete(index=user_input, mode=mode)
                print(f'\nYour Task {respond} {mode}d{self.s_END} !')
        except Exception as e:
            self.__exception_print(e)

    def json_handler(self, mode=''):
        try:
            _help, _prefix, mode = self.service.get_mode(mode=mode)
            print(f'\n{self.c_BLACK}{self.bg_WHITE}[ {mode[:4]} Tasker {_prefix} JSON ]{self.s_END}'
                  f'\n{self.s_ITALIC}*Enter a JSON name {_help}*{self.s_END}'
                  )
            user_input = input(f'{self.c_YELLOW}JSON name: {self.s_END}')
            name = self.service.json_handler(filename=user_input, mode=mode)
            print(f'\n{self.c_GREEN}File {self.c_BLUE}{name}{self.s_END}'
                  f' {self.c_GREEN}successfully {mode}d{self.s_END}'
                  )
        except Exception as e:
            self.__exception_print(e)

    def run(self):
        while True:
            print('_' * 20, f"\n{self.bg_BLACK}WELCOME TO TASKER !{self.s_END}")
            print('\n1. Tasks View')
            print('2. Task Add')
            print('3. Task Remove')
            print('4. Task Complete')
            print('5. Save to JSON')
            print('6. Load from JSON')
            print('Q. Exit')
            user_input = input(f'\n{self.c_YELLOW}Enter: {self.s_END}')

            if user_input.strip() == '1':
                self.view_tasks()
            if user_input.strip() == '2':
                self.add_task()
            if user_input.strip() == '3':
                self.remove_or_complete(mode='remove')
            if user_input.strip() == '4':
                self.remove_or_complete(mode='complete')
            if user_input.strip() == '5':
                self.json_handler(mode='save')
            if user_input.strip() == '6':
                self.json_handler(mode='load')
            if user_input.lower().strip() == 'q':
                exit('End program')
