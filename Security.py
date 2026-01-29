
class Security:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def value(self):
        return self.price * self.quantity


class Stock(Security):
    def __init__(self, symbol, price, quantity, dividend):
        super().__init__(symbol, price, quantity)
        self.dividend = dividend

    def dividend_income(self):
        return self.dividend * self.quantity


class Bond(Security):
    def __init__(self, symbol, price, quantity, interest_rate):
        super().__init__(symbol, price, quantity)
        self.interest_rate = interest_rate

    def yearly_interest(self):
        return self.value() * self.interest_rate


class Option(Security):
    def __init__(self, symbol, price, quantity, strike_price):
        super().__init__(symbol, price, quantity)
        self.strike_price = strike_price

    def is_profitable(self):
        return self.price > self.strike_price
