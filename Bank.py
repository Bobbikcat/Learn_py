class BankAccount:
    def __init__(self, value=0):
        if self.__check_type(value):
            self.__balance = value
        else:
            self.__balance = 0
            print('TypeError: Invalid value')

    def __getattr__(self, item):
        print(f'Error: Attribute "{item}" not Exist..')
        return None

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    @classmethod
    def __check_type(cls, deposit):
        return type(deposit) in (int, float)

    @property
    def balance(self):
        print(f'Your balance: {self.__balance}')
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance += amount

    @balance.deleter
    def balance(self):
        input_amt = float(input('Enter withdrawal Amount: '))
        if self.__balance >= input_amt:
            self.__balance -= input_amt
            print(f'Withdrawn: {input_amt}\nAvailable balance: {self.__balance}')
        else:
            user_choice = input(f'Account balance: {self.__balance}\nWithdraw everything ? (y/n): ')
            if user_choice.strip().lower() == 'y':
                self.__balance = 0
                print(f'Withdrawn full: {input_amt}\nAvailable balance: {self.__balance}')
            else:
                print('Cancel..')


def run():
    account_1 = BankAccount(100)

    while True:
        print('\nWelcome to Bank\n')
        print('1. View Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit\n')
        user_input = int(input('\nEnter an Action: '))

        if user_input == 1:
            respond = account_1.balance
        if user_input == 2:
            input_amt = float(input('Enter deposit Amount: '))
            account_1.balance = input_amt
        if user_input == 3:
            del account_1.balance
        if user_input == 4:
            exit('\nEnd program')


if __name__ == '__main__':
    run()
