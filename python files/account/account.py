class Account:

    def __init__(self, pin: int)-> None:
        self._pin = pin
        self.balance = 0

    def pin_is_valid(self, pin: int)-> bool:
        if pin == self._pin:
            return True
        return False

    def check_balance(self, pin: int)-> int:
        if self.pin_is_valid(pin):
            return self.balance
        else:
            return 0

    def deposit_fund(self, amount: int)-> None:
        if amount > 0:
            self.balance += amount

    def withdraw_fund(self, amount: int, pin: int)-> None:
        if 0 < amount <= self.balance and self.pin_is_valid(pin):
            self.balance -= amount

