def Divide(No1,No2):
    return No1 / No2

def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("enter second number:"))
    
    Ret = Divide(No1,No2)
    print("Division is:",Ret)

if __name__ == "__main__":
    main()