from money import Money

class Portfolio:
    def __init__(self):
        self.sum = 0

    def add(self, *moneys):
        for money in moneys:
            self.sum += money.amount

    def evaluate(self, currency):
        return Money(self.sum, currency)
