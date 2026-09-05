def LargestDigit():
    No = int(input("Enter The Number :"))

    No = abs(No)
    Largest = 0

    while No > 0:
        Digit = No % 10
        if Digit > Largest :
            Largest = Digit
            
        No = No // 10

    return Largest

def main():
    Ret = LargestDigit()
    print('Largets Digit :',Ret)

if __name__ == "__main__":
    main()