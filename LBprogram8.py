def ChkNum(No):
    if No > 0:
        print("Positive No")
    elif No < 0:
        print("Negative No")
    else:
        print("Zero")

    
def main():
    No = int(input("Enter a number :"))
    ChkNum(No)

if __name__ == "__main__":
    main()