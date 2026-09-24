def CountOdd():

    No = int(input("Enter The Number :"))

    no = abs(No)
    count = 0

    for digit in str(No):
        if int(digit) % 2 == 1:
            count = count + 1

    return count

def main():
    Ret = CountOdd()
    print("Count Of Odd Digits :",Ret)

if __name__ == "__main__":
    main()