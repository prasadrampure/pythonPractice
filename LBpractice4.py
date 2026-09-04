def Billing_Machine(c):

    Num = int(input("Enter invoiceNumber :"))

    if Num % 10 == 5:
        return True
    else:
        return False

def main():

    Ret = Billing_Machine()

    if Ret == True:
        print("Ends with 5")
    else:
        print("Does not End with 5")

if __name__ == "__main__":
    main()