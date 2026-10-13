def DifferenceMaxMin():
    N = int(input("enter N :"))

    if N <= 0:
        print("Invaid input")
        return

    Arr = list(map(int, input("Enter Array Elements :").split()))

    Max = Arr[0]
    Min = Arr[0]

    for i in range(1, N):
        if Arr[i] > Max:
            Max = Arr[i]

        if Arr[i] < Min:
            Min = Arr[i]

    Difference = Max - Min

    print("Difference :",Difference)

def main():
    DifferenceMaxMin()
    
if __name__ == "__main__":
    main()