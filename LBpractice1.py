def BankingPIN():

    pin = int(input("Enter The PIN :"))

    if 1000 <= pin <= 9999:
        print("Valid PIN")
    else:
        print("Invalid PID")

def main():
    BankingPIN()

if __name__ == "__main__":
    main()