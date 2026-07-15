Count = lambda No : True if No % 3 == 0 and No % 5 == 0 else False

def main():
    No = int(input("Enter a number :"))
    
    Ret = Count(No)
    if (Ret):
        print("No is divisible by 3&5")
    else:
        print("No is not divisible")
    

if __name__ == "__main__":
    main()