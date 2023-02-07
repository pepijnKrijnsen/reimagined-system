const { fail } = require("assert");
const Money = require("./money")

class Portfolio {
  constructor() {
    this.moneys = []
  }

  add(...moneys) {
    this.moneys = this.moneys.concat(moneys);
  }

  evaluate(bank, currency) {
    let failures = [];
    let total = this.moneys.reduce((sum, money) => {
      try {
        let convertedMoney = bank.convert(money, currency);
        return sum + convertedMoney.amount;
      }
      catch (error) {
        failures.push(error.message);
        return sum;
      }
    }, 0);
    if (failures.length) {
      throw new Error("Missing exchange rate(s): [" + failures.join() + "]");
    } else {  // else is required here because we don't want to return
      return new Money(total, currency);  // a Money in case of errors
    }
  }

}

module.exports = Portfolio;
