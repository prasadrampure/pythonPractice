def Largest(No1,No2,No3):
    if (No1 > No2) and (No1 > No3):
        return No1
    elif (No2 > No1) and (No2 > No3):
        return No2
    else:
        return No3

def main():
    No1 = int(input("Enter first number :"))
    No2 = int(input("Enter second number :"))
    No3 = int(input("Enter third number :"))

    Ret = Largest(No1,No2,No3)
    print("Largest no is :",Ret)


if __name__ == "__main__":
    main()