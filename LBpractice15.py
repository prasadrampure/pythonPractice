def ChkValid():
    No = int(input("Enter The Number :"))

    if No < 0 :
        return False

    Digit = No % 10
    No = No // 10

    while No > 0:
        NextDigit = No % 10

        if NextDigit != Digit:
            return False

        No = No // 10

    return True

def main():
    Ret = ChkValid()

    if Ret == True:
        print("Valid")
    else:
        print("Not Valid")
        
if __name__ == "__main__":
    main()