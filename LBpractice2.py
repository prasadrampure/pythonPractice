def Authentication():

    num = int(input("Enter The Number :"))

    if num % 2 == 0:
        print("Access Granted")
    else:
        print("Access Denied")
        
def main():
    Authentication()

if __name__ == "__main__":
    main()