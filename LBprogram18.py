def Table(No):
    for i in range(1,11):
        print(No*i)

def main():
    No = int(input("Enter a number :"))
    Ret = Table(No)
    print("Table is :",Ret)

if __name__ == "__main__":
    main()