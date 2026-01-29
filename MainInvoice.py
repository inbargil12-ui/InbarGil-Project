
from Invoice import Invoice


def main():
    number = input("Enter invoice number: ")
    customer = input("Enter customer name: ")
    date = input("Enter date: ")
    vat = float(input("Enter VAT (e.g. 0.17): "))
    paid = False

    inv = Invoice(number, customer, date, vat, paid)

    amount = float(input("Enter amount: "))
    inv.print_invoice(amount)


if __name__ == "__main__":
    main()
