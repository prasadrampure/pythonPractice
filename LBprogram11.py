def NaturalReverse(No):
    
    for i in range(No,0,-1):
        print(i)

def main():
    No = int(input("Enter a number :"))
    Ret = NaturalReverse(No)
    print("natural no is :",Ret)

if __name__ == "__main__":
    main()