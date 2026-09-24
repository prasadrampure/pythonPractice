def CountEven():

    No = int(input("Enter The Number :"))

    no = abs(No)
    count = 0

    for digit in str(No):
        if int(digit) % 2 == 0:
            count = count + 1

    return count

def main():
    Ret = CountEven()
    print("Count Of Even Digits :",Ret)

if __name__ == "__main__":
    main()