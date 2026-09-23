def ChkLastOdd():
    No = int(input("Enter The Digit :"))

    No = abs(No)

    Digit = No % 10

    if Digit % 2 == 1:
        return "Odd Ending"
    else:
        return "Even Ending"
    
def main():
    Ret = ChkLastOdd()
    print(Ret)

if __name__ == "__main__":
    main()