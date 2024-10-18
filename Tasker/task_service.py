class Service:
    def __init__(self, repository):
        self.repository = repository

    @staticmethod
    def __string_checker(argument):
        if type(argument) is not str:
            raise Exception('Argument must be <type: str>')
        if not len(argument.strip()):
            raise Exception('Empty argument string')

    @staticmethod
    def __index_checker(argument):
        if type(argument) is not int:
            raise Exception('Taken Argument not in <type: int>')

    def __task_adder(self, task_new):
        tasks = self.repository.view_tasks()
        if tasks:
            for index, value in tasks.items():
                if task_new.strip() in value.values():
                    raise Exception('This task already Exist..')
            else:
                self.repository.add_task(task_new)
        else:
            self.repository.add_task(task_new)

    def add_task(self, description=''):
        self.__string_checker(description)
        self.__task_adder(description)

    def view_tasks(self):
        tasks = self.repository.view_tasks()
        if tasks:
            for index, value in tasks.items():
                if value['completed']:
                    print(f'\033[32m{index}. {value['description']}\033[0m')  # GREEN
                else:
                    print(f'\033[31m{index}. {value['description']}\033[0m')  # RED
        else:
            raise Exception('This Tasker is empty..')

    def remove_or_complete(self, index=0, mode=''):
        self.__index_checker(index)
        self.__string_checker(mode)
        if index in self.repository.view_tasks():
            notation = eval(f'self.repository.{mode.lower()}_task(index=index)')
            return notation
        else:
            raise Exception(f'Task for {mode.lower()} - not found..')

    def get_mode(self, mode=''):
        _help = _prefix = ''
        self.__string_checker(mode)
        mode = mode.title().strip()
        if mode in self.repository.get_mode():
            if mode == 'Load':
                mode += 'e'
                _prefix = 'from'
            elif mode == 'Save':
                _prefix = 'to'
                _help = '(up to 16 characters)'
            return _help, _prefix, mode
        else:
            raise Exception('*Invalid "mode" Value*')

    def json_handler(self, filename='', mode=''):
        self.__string_checker(filename)
        self.__string_checker(mode)
        filename = filename.strip().lower()
        mode = mode[:4].lower()
        if mode == 'save':
            if len(filename) <= 16:
                if self.repository.view_tasks():
                    pass
                else:
                    raise Exception('This Tasker is empty..')
            else:
                raise Exception('Name length > 16..')
        if mode == 'save' or mode == 'load':
            if filename[-5:] != '.json':
                filename = filename + '.json'
            eval(f'self.repository.{mode}_json(filename)')
            return filename
        else:
            raise Exception('*Invalid "mode" Value*')
