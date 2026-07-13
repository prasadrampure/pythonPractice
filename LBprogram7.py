def ChkEven(No):
    if No % 2 == 0:
        return True
    else:
        return False

def main():
    No = int(input("Enter a number"))
    Ret = ChkEven(No)
    if(Ret):
        print("No is Even")
    else:
        print("No is Odd")

if __name__ == "__main__":
    main()