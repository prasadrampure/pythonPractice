def Palindrome():

    No = int(input("Enter Transaction Number :"))

    if No < 0:
        print("Not Palindrome")

    Original = No
    Reverse = 0

    while No > 0:
        Digit = No % 10
        Reverse = Reverse * 10 + Digit
        No = No // 10

    if Original == Reverse:
        return True
    else:
        return False
    
def main():
    Ret = Palindrome()

    if Ret == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()