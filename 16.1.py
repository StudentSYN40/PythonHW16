class CashRegister:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def top_up(self, amount):
        if amount >= 0:
            self.balance += amount
            return f"Успешно пополнено на {amount} денег"
        else:
            return "Сумма должна быть положительной"

    def count_1000(self):
        return self.balance // 1000

    def take_away(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Успешно взято {amount} денег"
        else:
            return "Недостаточно денег"

initial_balance = 5000
cash_register = CashRegister(initial_balance)

print(cash_register.top_up(2555))
print(cash_register.count_1000())
print(cash_register.take_away(4000))
print(cash_register.take_away(5000))
