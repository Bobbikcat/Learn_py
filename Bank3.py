class BankAccount:
    def __init__(self, value=0):
        # self.__balance = 0
        # Я добавил присвоение сюда,
        # чтобы не писать Else с этим присвоением. Ведь Если __check_type будет провален
        # и будет выдан Raise, тогда у объекта класса не будет атрибута __balance.
        # Ecли написать тут Else, тогда в __check_type придется Raise заменить Принтом,
        # а перенести присвоение в блок Else в __check_type не получится, ведь метод статичный,
        # (и нелогично, даже если бы он был обычным).
        if self.__check_type(value):
            self.__balance = value
        else:
            self.__balance = 0

    @staticmethod
    def __check_type(deposit):
        if type(deposit) in (int, float):
            return True
        # raise TypeError('TypeError: Invalid value..')
        else:
            # Насчёт предыдущей версии:
            # Зачем тут Else, если тут либо Return сработал бы, либо Raise.
            print('\nTypeError: Invalid value..')

    @property
    def balance(self):
        print(f'Your balance: {self.__balance}')
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if self.__check_type(amount):
            self.__balance += abs(amount)

    def withdraw(self):
        input_amt = abs(float(input('Enter withdrawal Amount: ')))
        if self.__balance >= input_amt:
            self.__balance -= input_amt
            print(f'Withdrawn: {input_amt}\nAvailable balance: {self.__balance}')
        else:
            if self.__balance > 0:
                user_choice = input(f'Account balance: {self.__balance}\nWithdraw everything ? (y/n): ')
                if user_choice.strip().lower() == 'y':
                    self.__balance = 0
                    print(f'Withdrawn full.\nAvailable balance: {self.__balance}')
                else:
                    print('Cancel..')
            else:
                print('\nNot enough founds..')


def run():
    account_1 = BankAccount(100)
    # acc_example = BankAccount('example')
    # print(acc_example.balance)

    while True:
        print('\nWelcome to Bank\n')
        print('1. View Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit\n')
        try:
            user_input = int(input('\nEnter an Action: '))

            if user_input == 1:
                respond = account_1.balance
            if user_input == 2:
                input_amt = float(input('Enter deposit Amount: '))
                account_1.balance = input_amt
            if user_input == 3:
                account_1.withdraw()
            if user_input == 4:
                exit('\nEnd program')
        except Exception:
            print('\nError: Invalid input..')


if __name__ == '__main__':
    run()
