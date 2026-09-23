def CountTotalDigit():
    No = int(input("Enter serialNumber :"))

    No = abs(No)

    if No == 0:
        return 1

    count = 0

    while No > 0:
        count = count + 1
        No = No // 10

    return count

def main():
    Ret = CountTotalDigit()
    print("Total Digits :",Ret)

if __name__ == "__main__":
    main()