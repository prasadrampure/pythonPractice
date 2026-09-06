def ArmstrongValidator():

    No = int(input("Enter The Number :"))

    Original = No
    Count = 0
    Sum = 0

    while No > 0:
        Count = Count + 1
        No = No // 10

    No = Original

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit ** Count
        No = No // 10

    if Sum == Original:
        return True
    else:
        return False

def main():
    Ret = ArmstrongValidator()

    if Ret == True:
        print("Armstrong")
    else:
        print("Not Armstrong")

if __name__ == "__main__":
    main()