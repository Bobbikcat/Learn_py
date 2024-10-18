import json


class Repository:
    def __init__(self):
        self.__menu_mods = ['Complete', 'Remove', 'Save', 'Load']
        self.__task_dict = {}
        self.__temp_dict = {}

    def get_mode(self):
        return self.__menu_mods

    def add_task(self, task_new):
        self.__task_dict[len(self.__task_dict) + 1] = {
            'description': task_new.strip(),
            'completed': False
        }

    def complete_task(self, index):
        self.__task_dict[index]['completed'] = True
        return 'marked as\033[32m'

    def view_tasks(self):
        return self.__task_dict

    def remove_task(self, index):
        del self.__task_dict[index]
        for index, (k, v) in enumerate(self.__task_dict.items(), start=1):
            self.__temp_dict[index] = v
        self.__task_dict.clear()
        self.__task_dict.update(self.__temp_dict)
        self.__temp_dict.clear()
        return 'has been\033[33m'

    def save_json(self, filename):
        with open(f'{filename}', 'w') as file:
            json.dump(self.__task_dict, file, indent=4)  # Почему ругается, не пойму :()

    def load_json(self, filename):
        try:
            with open(f'{filename}', 'r') as file:
                self.__task_dict = self.__check_json(json.load(file))
        except json.JSONDecodeError:
            raise Exception('Invalid JSON file..')
        except FileNotFoundError:
            raise Exception('File not Found..')
        except Exception:
            raise Exception('Incompatible Json file..')

    @staticmethod
    def __check_json(data):
        temp_data = {}
        if type(data) is dict:
            for index, (k, v) in enumerate(data.items(), start=1):
                if type(int(k)) is not int or type(v) is not dict:
                    break
                if len(v) != 2:
                    break
                if not v['description'] or type(v['completed']) is not bool:
                    break
                temp_data[index] = v
            else:
                return temp_data
            raise Exception('Incompatible Json file..')
        else:
            raise Exception('Incompatible Json file..')
