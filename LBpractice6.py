def CheckNum():

    Num = int(input("Enter The Number :"))

    if Num > 0 :
        print("Positive Number")
    elif Num < 0 :
        print("Negative Number")
    else:
        print("Zero")

def main():
    CheckNum()

if __name__ == "__main__":
    main()