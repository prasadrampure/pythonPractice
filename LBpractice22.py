def CheckSequre():
    No = int(input("Enter The Number : "))

    if No < 0:
        return "Invalid"

    if No < 10:
        return "Valid"

    prev = No % 10
    No = No // 10

    while No > 0:
        Digit = No % 10

        if Digit >= prev:
            return "Invalid"

        prev = Digit
        No = No // 10

    return "Valid"

def main():
    Ret = CheckSequre()
    print("Result :",Ret)

if __name__ == "__main__":
    main()