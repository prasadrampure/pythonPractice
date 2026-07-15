def Mult(No1,No2):
    for i in range(1,No2+1):
        print(No1*i)

def main():
    No1 = int(input("Enter a number :"))
    No2 = int(input("Enter a number :"))
    Mult(No1,No2)
    

if __name__ == "__main__":
    main()