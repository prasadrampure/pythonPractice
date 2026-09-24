def ChkDigit():

    No = int(input("Enter The Number :"))

    No = abs(No)

    for digit in str(No):
        if digit == "5":
            return "Digit Found"

    return "Not Found"

def main():
    Ret = ChkDigit()
    print(Ret)

if __name__ == "__main__":
    main()