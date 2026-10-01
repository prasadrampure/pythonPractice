def DigitLockValidator():

    No = int(input("Enter The Digit :"))

    No = abs(No)

    if No == 0:
        print("Lock Denied")
    else:
        while No > 0:
            digit = No % 10

            if digit == 0:
                print("Lock Denied")
                break

            No = No // 10
        else:
            print("Lock Open")

def main():
    DigitLockValidator()

if __name__ == "__main__":
    main()