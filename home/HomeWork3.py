class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __str__(self):
        return f'name: {self._name}n'\
               f'balance: {self._balance}\n'
    def moneyX(self):
        print(self._balance + (int(input(f"Введите сумму денег:"))))

    def _kill(self):
        print(self._balance is None)
    def __jackpot(self):
        print(self._balance * 10)
        self.__jackpot()
    def _plus(self, other):
        print(self._balance + other.balance)
bank1 = Bank(balance=0, name = 'Maga')
bank2 = Bank(balance=21500, name='Ben')
print(bank1, bank2)
bank1.moneyX()
bank2.moneyX()
bank1._kill()
bank2._kill()
