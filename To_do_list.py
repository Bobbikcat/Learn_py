class ToDoList:
    task_list = {'To do something': '', }

    def __init__(self):
        pass

    def list_tasks(self):
        if self.task_list:
            print('\n[ To-do list ]')
            for index, (k, v) in enumerate(self.task_list.items(), start=1):
                print(f'[{index}] {k} {v.strip()}')
            print('\n( completed tasks marked with * )')
        else:
            raise Exception('\n" To-do list is empty ! "')

    def add_task(self, task):
        if task.strip() not in self.task_list:
            self.task_list[task] = ''
            print(f'\nThe New task added')
        else:
            print('\nThis task already exist !')

    def remove_task(self, task):
        for index, (k) in enumerate(self.task_list, start=1):
            try:
                if index == int(task):
                    del self.task_list[k]
                    print(f'\nThe task №{task.strip()} has been removed')
                    return
            except Exception:
                print('\nERROR: Invalid input')
                return
        raise Exception('\nERROR: Task not found')

    def complete_task(self, task):
        for index, (k) in enumerate(self.task_list, start=1):
            try:
                if index == int(task):
                    self.task_list[k] = "*"
                    print(f'\nThe task №{task.strip()} has been marked as  * completed *')
                    return
            except Exception:
                print('\nERROR: Invalid input')
                return
        raise Exception('\nERROR: Task not found')
