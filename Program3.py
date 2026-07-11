def Reverse(No):
    
    while(No != 0):
        print(No)
        No = No - 1
def main():


        No = int(input("Enter a number:"))

        Ret = Reverse(No)
        print("Reverse is:",Ret)
    

if __name__ == "__main__":
    main()