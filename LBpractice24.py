def ChkFirstDigit():
    No = int(input("Enter The Number :"))

    No = abs(No)

    if No == 0:
        return 0

    while No >= 10:
        No = No // 10

    return No

def main():
    Ret = ChkFirstDigit()
    print("First Digit :",Ret)

if __name__ == "__main__":
    main()