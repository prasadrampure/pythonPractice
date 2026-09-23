def SumDigits():
    No = int(input("Enter Invoice Number :"))

    No = abs(No)
    Sum = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Ret = SumDigits()
    print("Sum Of Digits :",Ret)

if __name__ == "__main__":
    main()