def Even(No):
    
    for i in range(1, No+1):
        if i % 2 == 0:
            print(i)
        
def main():
    No = int(input("Enter a number :"))
    Ret = Even(No)
    print("Even no is :",Ret)

if __name__ == "__main__":
    main()