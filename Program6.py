def Factor(No):
    Mult = 1
    for i in range(1,No):
        if (No % i == 0):
            Mult = Mult * i
    return Mult
        
    

def main():

    No = int(input("Enter a number :"))
    Ret = Factor(No)
    print("Factor mult is :",Ret)

if __name__ == "__main__":
    main()