#  start program
from HW_Library.Console import Console
from HW_Library.Repository import Repository
from HW_Library.Service import Service
from HW_Library.Validator import Validator


def main():
    repository = Repository()
    validator = Validator()
    service = Service(repository, validator)
    console = Console(service)

    console.run()


if __name__ == '__main__':
    main()
