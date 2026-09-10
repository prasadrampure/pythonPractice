def StrongTransaction():
    No = int(input("Enter The Transaction Number :"))

    if No < 0:
        print("Week Transaction")

    if No == 0:
        DigitCount = 1
        Sum = 1
    else:
        DigitCount = 0
        Sum = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        DigitCount = DigitCount + 1
        No = No // 10

    if Sum % DigitCount == 0:
        return "Strong Transaction"
    else :
        return "Week Transaction"

    
def main():
    Ret = StrongTransaction()
    print(Ret)
   
if __name__ == "__main__":
    main()