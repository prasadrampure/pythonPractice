def CheckPrefect():
    No = int(input("Enter The Number :"))

    if No <= 0:
        return False

    Sum = 0
    i = 1

    while i < No:
        if No % i == 0:
            Sum = Sum + i

        i = i + 1

    if Sum == No :
        return True
    else:
        return False

def main():
    Ret = CheckPrefect()

    if Ret == True:
        print("Prefect")
    else:
        print("Not Perfect")

if __name__ == "__main__":
    main()