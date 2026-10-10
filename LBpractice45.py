def CountEvenArr():

    N = int(input("Enter N :"))

    Arr = list(map(int, input("Enter Array Elements :").split()))

    if N <= 0 :
        print("Invalid Input")

    else:
        count = 0

        for i in Arr:
            if i % 2 == 0:
                count += 1

        print("Count of Even Numbers :",count)
        
def main():
    CountEvenArr()

if __name__ == "__main__":
    main()