def SumDigits():

    Num = int(input("Enter The Number :"))

    Num = abs(Num)
    Sum = 0

    while Num > 0:
        Digit = Num % 10
        Sum = Sum + Digit
        Num = Num // 10

    print("Sum of Digits :",Sum)

def main():
    SumDigits()

if __name__ == "__main__":
    main()