def Natural(No):
    
    for i in range(1, No+1):
        print(i)

def main():
    No = int(input("Enter a number :"))
    Ret = Natural(No)
    print("natural no is :",Ret)

if __name__ == "__main__":
    main()