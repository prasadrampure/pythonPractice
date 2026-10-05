def SumProduct():

    No = int(input("Enter the number :"))

    No = abs(No)

    sum = 0
    product = 1

    while No > 0:
        digit = No % 10

        sum = sum + digit
        product = product * digit

        No = No // 10

    if sum == product:
        print("Valid Number")
    else:
        print("Invalid Number")

def main():
    SumProduct()

if __name__ == "__main__":
    main()