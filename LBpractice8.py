def CheckNum():

    Num = int(input("Enter The Number :"))

    LastDigit = Num % 10

    if LastDigit % 2 == 0:
        return True
    else:
        return False
    
def main():
    Ret = CheckNum()

    if Ret == True:
        print("Last Digit Even")
    else:
        print("last Digit Odd")

if __name__ == "__main__":
    main()