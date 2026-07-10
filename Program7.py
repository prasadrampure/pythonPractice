def Reverse_Factor(No):
    i = No // 2
    while(i >= 1):
        if No % i == 0:
               sprint(i)
        i = i - 1

def main():
    No = int(input("Enter a number :"))

    Ret = Reverse_Factor(No)
    print("Reverse factor is :",Ret)

if __name__ == "__main__":
    main()