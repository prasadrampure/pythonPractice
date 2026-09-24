def PrintDigits():

    No = int(input("Enter the Digits :"))

    No = abs(No)

    for digit in str(No):
        print(digit, end=" ")

def main():
    PrintDigits()

if __name__ == "__main__":
    main()