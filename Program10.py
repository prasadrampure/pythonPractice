def main():
    No = int(input("Enter a number :"))

    if No % 4 == 0 and No % 100 != 0:
        print("Leap year")
    elif No % 100 != 0:
        print("It is not leap year")
    
if __name__ == "__main__":
    main()