def Maximum(No1,No2):
    if No1 > No2:
        return No1 
    else:
        return No2
    

def main():
    No1 = int(input("Enter first number :"))
    No2 = int(input("Enter second number :"))
    Ret = Maximum(No1,No2)
    print("Maximum no is :",Ret)
    
if __name__ == "__main__":
    main() 