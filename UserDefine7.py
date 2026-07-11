def Calculation(value1,value2):
    Add = value1 + value2
    Sub = value1 - value2
    return Add,Sub

def main():
    value1 = int(input("Enter First number : "))
    value2 = int(input("Enter Second number : "))

    Ret1,Ret2 = Calculation(value1,value2)

    print("Addition is :",Ret1)
    print("Substraction is :",Ret2)

if __name__ == "__main__":
    main()