def Product():

    No = int(input("Enter The Number :"))

    No = abs(No)
    product = 1
    Found = False

    while No > 0:
        digit = No % 10

        if digit != 0:
            product = product * digit
            Found = True

        No = No // 10

    if Found:
        print("Product Value :",product)
    else:
        print("Product Value : 0")

def main():
    Product()

if __name__ == "__main__":
    main()