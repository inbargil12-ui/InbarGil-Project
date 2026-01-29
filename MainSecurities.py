
from Security import Stock, Bond, Option


def main():
    stock = Stock(
        input("Stock symbol: "),
        float(input("Stock price: ")),
        int(input("Quantity: ")),
        float(input("Dividend per unit: "))
    )

    bond = Bond(
        input("\nBond symbol: "),
        float(input("Bond price: ")),
        int(input("Quantity: "))
        ,
        float(input("Interest rate: "))
    )

    option = Option(
        input("\nOption symbol: "),
        float(input("Option price: ")),
        int(input("Quantity: ")),
        float(input("Strike price: "))
    )

    print("\n--- Stock ---")
    print("Total value:", stock.value())
    print("Dividend:", stock.dividend_income())

    print("\n--- Bond ---")
    print("Total value:", bond.value())
    print("Interest:", bond.yearly_interest())

    print("\n--- Option ---")
    print("Total value:", option.value())
    print("Profitable:", option.is_profitable())


if __name__ == "__main__":
    main()
