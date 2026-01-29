
def is_multiple(a, b):
    if a == 0 or b == 0:
        return False
    return a % b == 0 or b % a == 0


def main():
    print("Multiple Check Program")
    print("Enter -1 to exit\n")

    while True:
        try:
            num1 = int(input("Enter first number: "))
            if num1 == -1:
                print("Exiting the program.")
                break

            num2 = int(input("Enter second number: "))

            if is_multiple(num1, num2):
                print("One number is a multiple of the other.\n")
            else:
                print("Neither number is a multiple of the other.\n")

        except ValueError:
            print("Error: please enter integers only.\n")


if __name__ == "__main__":
    main()
