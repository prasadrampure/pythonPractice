def Product(No):

    product = 1
    for i in range(1 , No+1):
        product = product * i

    return product
        
    

def main():
    No = int(input("Enter a number :"))
    Ret = Product(No)
    print('Product is :',Ret)


if __name__ == "__main__":
    main()