def Counter():
    Num = int(input("Enter the Number :"))

    counter = 0

    while Num > 0:
        Digit = Num % 10

        if Digit == 0:
            counter = counter + 1

        Num = Num // 10

    print("Count Of Zero Digits :",counter)
    
def main():
    Counter()

if __name__ == "__main__":
    main()