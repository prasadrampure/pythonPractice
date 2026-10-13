def SearchElement():

    N = int(input("Enter N :"))

    if N <= 0 :
        print("Invaid Input")
        return

    Arr = list(map(int, input("Enter Array Elements :").split()))

    target = int(input("Enter Target :"))

    for i in range(N):
        if Arr[i] == target:
            print("Found")
            return

    print("Not Found")
    
def main():
    SearchElement()

if __name__ == "__main__":
    main()