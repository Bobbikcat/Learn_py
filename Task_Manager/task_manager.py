import json


class TaskManager:
    def __init__(self):
        self.tasks = []

    def view_tasks(self):
        if self.tasks:
            for i, el in enumerate(self.tasks, start=1):
                print(f'{i}. {el['description']} | Status: {el['completed']}')
            else:
                return True
        else:
            print('- Empty -')
            return None

    def add_task(self, description):
        self.tasks.append({
            'description': description,
            'completed': False
        })
        print('* Added *')

    def remove_task(self, index):
        if len(self.tasks) >= index > 0:
            del self.tasks[index - 1]
            print('* Removed *.')
        else:
            print('- Not found -')

    def complete_task(self, index):
        if len(self.tasks) >= index > 0:
            self.tasks[index - 1]['completed'] = True
            print('* Marked as complete *')
        else:
            print('- Not found -')

    def save_to_json(self, filename):
        with open(f'{filename}.json', 'w') as file:
            json.dump(self.tasks, file, indent=4)  # все еще не понимаю, почему ругается
            print('* Saved *')

    def load_from_json(self, filename):
        try:
            with open(f'{filename}.json', 'r') as file:
                self.tasks = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print('Error: File: Invalid / Not Found')


if __name__ == '__main__':
    tasker = TaskManager()
    while True:
        print('\nTASKER\n')
        print('\n1. Tasks View')
        print('2. Task Add')
        print('3. Task Remove')
        print('4. Task Complete')
        print('5. Save to JSON')
        print('6. Load from JSON')
        print('Q. Exit')
        user_input = input(f'\nEnter: ')
        print('____________')

        if user_input.strip() == '1':
            tasker.view_tasks()
        if user_input.strip() == '2':
            task = input('\nTask: ')
            tasker.add_task(task)
        if user_input.strip() == '3':
            respond = tasker.view_tasks()
            if respond is not None:
                task = int(input('\nNumber: '))
                tasker.remove_task(task)
        if user_input.strip() == '4':
            respond = tasker.view_tasks()
            if respond is not None:
                task = int(input('\nNumber: '))
                tasker.complete_task(task)
        if user_input.strip() == '5':
            respond = tasker.view_tasks()
            if respond is not None:
                task = input('\nName (with no ".json")\n>>> ')
                tasker.save_to_json(task)
        if user_input.strip() == '6':
            task = input('\nName (with no ".json")\n>>> ')
            tasker.load_from_json(task)
        if user_input.lower().strip() == 'q':
            exit('End program')
