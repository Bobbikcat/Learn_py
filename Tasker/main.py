from Tasker.task_repository import Repository
from Tasker.task_service import Service
from Tasker.Task_manager import TaskManager


def main():
    repository = Repository()
    service = Service(repository)
    console = TaskManager(service)
    console.run()

if __name__ == '__main__':
    main()