
class Invoice:
    def __init__(self, number, customer, date, vat, paid):
        self.__number = number
        self._customer = customer
        self.date = date
        self.vat = vat
        self.paid = paid

    @property
    def number(self):
        return self.__number

    @property
    def customer(self):
        return self._customer

    def total(self, amount):
        return amount * (1 + self.vat)

    def print_invoice(self, amount):
        print("Invoice number:", self.number)
        print("Customer:", self.customer)
        print("Date:", self.date)
        print("Total:", self.total(amount))
