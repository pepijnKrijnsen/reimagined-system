from money import Money

class Portfolio:
    def __init__(self):
        self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys = [ money for money in moneys ]

    def evaluate(self, currency):
        sum = 0
        for money in self.moneys:
            if currency == money.currency:
                sum += money.amount
            else:
                sum += self._convert(money, currency)
        return Money(sum, currency)

    def _convert(self, money, currency):
        return money.amount * self._eur_to_usd
