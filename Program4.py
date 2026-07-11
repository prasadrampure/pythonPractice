def Divisible(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    No = int(input("Enter a number:"))
    Ret = Divisible(No)
    if Ret == True:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")
    

if __name__ == "__main__":
    main()