def ChkPairSum():

    Arr = list(map(int, input("Enter Aarray Elements :").split()))
    T = int(input("Enter Target Value :"))

    for i in range(len(Arr)):
        for j in range(i + 1, len(Arr)):
            if Arr[i] + Arr[j] == T:
                print("Pair Exist")
                return

    print("Not Exist")

def main():
    ChkPairSum()

if __name__ == "__main__":
    main()