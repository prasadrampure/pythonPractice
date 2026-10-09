def ChkCostlyPrice():

    N = int(input("Enter N :"))

    prices = list(map(int, input("Enter Prices :").split()))

    if N <= 0:
        print("Invalid Input")
    else:

        count = 0

        for price in prices:
            if price >= 1000:
                count = count + 1

        print("Count of costly items :",count)

def main():
    ChkCostlyPrice()

if __name__ == "__main__":
    main()