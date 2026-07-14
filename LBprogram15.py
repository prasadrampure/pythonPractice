def SumEven(No):

    sum = 0
    for i in range(1 , No+1):
        if i % 2 == 0:
            print(i)
        
            sum = sum + i

    return sum


def main():
    No = int(input("Enter a number :"))
    Ret = SumEven(No)
    print('Sum is :',Ret)


if __name__ == "__main__":
    main()