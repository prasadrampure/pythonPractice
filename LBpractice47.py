def ReplaceNegativeNo():

    Arr = list(map(int, input("Enter Array Elements :").split()))

    for i in range(len(Arr)):
        if Arr[i] < 0:
            Arr[i] = 0

    print("Updated Array :",Arr)

def main():
    ReplaceNegativeNo()

if __name__ == "__main__":
    main()