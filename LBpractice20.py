def ReplaceZero():
    No = input("Enter The Number :")

    if No == "0":
        return "1"

    Result = ""

    for digit in No:
        if No == "0":
            Result = Result + "1"
        else:
            Result = Result + digit

    return Result

def main():
    Ret = ReplaceZero()
    print("Replace Number :",Ret)

if __name__ == "__main__":
    main()