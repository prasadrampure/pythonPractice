def Summation(Data):
    Sum = 0 
    for no in Data:
        Sum = Sum + no

    return Sum

def main():
    Marks = [55,35,25,85,105]

    Ret = Summation(Marks)

    print("Addition is :",Ret)

if __name__ == "__main__":
    main()