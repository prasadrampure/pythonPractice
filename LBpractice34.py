def SumEvenPosition():

    No = int(input("Enter The Digit :"))

    No = abs(No)

    position = 1
    sum = 0

    while No > 0:
        digit = No % 10

        if position % 2 == 0:
            sum = sum + digit

        No = No // 10
        position = position + 1

    return sum

def main():
    Ret = SumEvenPosition()
    print("Sum of Even Position Digit :",Ret)

if __name__ == "__main__":
    main()