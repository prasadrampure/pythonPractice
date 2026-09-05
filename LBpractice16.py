def SumEven():

    No = int(input("Enter The Number :"))

    Sum = 0

    while No > 0:
        Digit = No % 10

        if Digit % 2 == 0:
            Sum = Sum + Digit

        No = No // 10

    return Sum

def main():
    Ret = SumEven()
    print("Sum of Even Digits :",Ret)

if __name__ == "__main__":
    main()