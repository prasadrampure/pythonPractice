def Count(No):
    count = 0
    for i in range(1,No+1):
        if i % 3 == 0:
            count = count+1

    return count

        

def main():
    No = int(input("Enter a number :"))
    
    Ret = Count(No)
    print("count is :",Ret)
    

if __name__ == "__main__":
    main()