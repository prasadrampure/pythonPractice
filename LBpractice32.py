def SmallestNum():

    No = int((input("Enter The Number :")))

    No = abs(No)

    if No < 10:
        return No

    smallest = 9

    while No > 0:
        digit = No % 10

        if digit < smallest:
            smallest = digit

        No = No // 10
    
    return smallest

def main():
    Ret = SmallestNum()
    print("Smallest digit :",Ret)

if __name__ == "__main__":
    main()