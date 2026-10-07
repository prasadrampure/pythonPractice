def CalculateMaxWeight():
    N = int(input("Enter N :"))

    weights = list(map(int, input("Enter Weights :").split()))

    if N <= 0:
        print("Invalid Input")
    else:
        maximum = weights[0]

        for i in range(1,N):
            if weights[i] > maximum:
                maximum = weights[i]

        print("Maximum Weights :",maximum)
  
def main():
    CalculateMaxWeight()

if __name__ == "__main__":
    main()