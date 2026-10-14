def CountDivisible():

    Arr = list(map(int, input("Enter Array Elements :").split()))

    count = 0

    for i in range(len(Arr)):
        if Arr[i] % 3 == 0 and Arr[i] % 5 == 0:
            count += 1

    print("Count :",count)

def main():
    CountDivisible()
    
if __name__ == "__main__":
    main()