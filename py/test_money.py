import unittest

from money import Money
from portfolio import Portfolio

class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(tenEuros.times(2), twentyEuros)

    def testDivision(self):
        original_money = Money(4002, "KRW")
        actual_money_after_division = original_money.divide(4)
        expected_money_after_division = Money(1000.5, "KRW")
        self.assertEqual(actual_money_after_division,
                         expected_money_after_division)

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

    def testAdditionOfDollarsAndEuros(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expected_value = Money(17, "USD")
        actual_value = portfolio.evaluate("USD")
        self.assertEqual(actual_value, expected_value,
                         f"{actual_value} != {expected_value}")

    def testAdditionOfDollarsAndWons(self):
        oneDollar = Money(1, "USD")
        elevenHundredWons = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(oneDollar, elevenHundredWons)
        expected_value = Money(2200, "KRW")
        actual_value = portfolio.evaluate("KRW")
        self.assertEqual(actual_value, expected_value,
                         f"{actual_value} != {expected_value}")

    def testAdditionWithMultipleMissingExchangeRates(self):
        oneDollar = Money(1, "USD")
        oneEuro = Money(1, "EUR")
        oneWon = Money(1, "KRW")
        portfolio = Portfolio()
        portfolio.add(oneDollar, oneEuro, oneWon)
        with self.assertRaisesRegex(
                Exception,
                "Missing exchange rate\(s\):\[USD->Kalganid, EUR->Kalganid, KRW->Kalganid\]"
                ):
            portfolio.evaluate("Kalganid")

if __name__ == "__main__":
    unittest.main()
