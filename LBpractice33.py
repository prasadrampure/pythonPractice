def Frequency(No,d):

    No = abs(No)
    count = 0

    if No == 0 and d == 0:
        return 1

    while No > 0:
        digit = No % 10

        if digit == d:
            count = count + 1

        No = No // 10

    return count 

def main():
    No = int(input("Enter Number :"))
    d = int(input("Enter Digit :"))

    result = Frequency(No,d)
    print("Frequency of Digit :",result)

if __name__ == "__main__":
    main()