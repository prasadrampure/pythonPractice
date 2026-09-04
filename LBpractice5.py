def SecurityCheck():

    Num = int(input("Enter The Number :"))

    if Num % 3 == 0 and Num % 5 == 0:
        return True
    else:
        return False

def main():
    Ret = SecurityCheck()

    if Ret == True:
        print("Valid Number")
    else:
        print("invalid Number")

if __name__ == "__main__":
    main()