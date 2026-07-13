def ChkNum(No):
    if No > 0:
        return 1
    elif No < 0:
        return 2
    else:
        return 3

def main():
    No = int(input("Enter a number :"))
    Ret = ChkNum(No)
    if(Ret == 1):
        print("Positive")
    elif(Ret == 2):
        print("Negative")
    else:
        print("Zero")
    
        
    

if __name__ == "__main__":
    main()