def CountPositiveNegative():

    Arr = list(map(int, input("Enter Array Elements :").split()))

    PositiveCount = 0
    NegativeCount = 0

    for i in range(len(Arr)):
        if Arr[i] > 0:
            PositiveCount += 1
        if Arr[i] < 0:
            NegativeCount += 1

    print("Positive Count :",PositiveCount)
    print("Negative Count :",NegativeCount)
    
def main():
    CountPositiveNegative()
    
if __name__ == "__main__":
    main()