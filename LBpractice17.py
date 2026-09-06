def ProductOdd():
    No = int(input("Enter The Number :"))

    No = abs(No)
    product = 1
    Found = False

    while No > 0:
        Digit = No % 10

        if Digit % 2 != 0 :
            product = product * Digit
            Found = True

        No = No // 10

    if Found == False:
        return 0
    
    return product

def main():
    Ret = ProductOdd()
    print("Product of Odd Digits :",Ret)

if __name__ == "__main__":
    main()