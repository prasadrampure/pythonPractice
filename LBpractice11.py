def ReverseNum(Num):

    if Num == 0:
        return Num
    
    Sign = 1

    if Num < 0:
        Sign = -1
        Num = abs(Num)

    Rev = 0

    while Num != 0:
        digit = Num % 10
        Rev = Rev * 10 + digit
        Num = Num // 10

    return Sign * Rev

def main():
    Num = int(input("Enter The Number :"))

    Ret = ReverseNum(Num)
    print("Reverse is :",Ret)

if __name__ == "__main__":
    main()