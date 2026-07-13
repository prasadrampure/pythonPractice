def Marks(Sub1,Sub2,Sub3,Sub4,Sub5):
    return Sub1+Sub2+Sub3+Sub4+Sub5
    

def main():

    Sub1 = int(input("Sub 1 :"))
    Sub2 = int(input("Sub 2 :"))
    Sub3 = int(input("Sub 3 :"))
    Sub4 = int(input("Sub 4 :"))
    Sub5 = int(input("Sub 5 :"))

    Ret = Marks(Sub1,Sub2,Sub3,Sub4,Sub5)
    print("Total Marks :",Ret)
    Average = Ret / 5
    print("Average",Average)


if __name__ == "__main__":
    main()