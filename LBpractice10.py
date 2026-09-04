def CheckNum():

    Num = int(input("Enter The Batch Number :"))

    if Num % 10 == 0:
        return True
    else:
        return False
    
def main():
    Ret = CheckNum()

    if Ret == True:
        print("Priority Batch")
    else:
        print("Normal Batch")

if __name__ == "__main__":
    main()