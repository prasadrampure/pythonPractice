def CalculateMiniTemp():
    N = int(input("Enter N :"))

    temps = list(map(int, input("Enter Tempreture :").split()))

    if N <= 0:
        print("Invalid Input")
    else:
        minimum = temps[0]

        for i in range(1, N):
            if temps[i] < minimum:
                minimum = temps[i]

        print("Minimum Tempreture :",minimum)

def main():
    CalculateMiniTemp()

if __name__ == "__main__":
    main()