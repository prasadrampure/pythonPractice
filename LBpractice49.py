def CountUniqueElements():

    Arr = list(map(int, input("Enter Array Elements :").split()))

    Unique = set(Arr)

    print("Number Of Unique Elements :",len(Unique))

def main():
    CountUniqueElements()

if __name__ == "__main__":
    main()